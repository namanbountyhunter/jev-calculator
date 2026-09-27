from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from jev_service import decide_operation
from calculator import calculate
from number_parser import extract_numbers
from tool_registry import execute_tool


app = FastAPI(title="Jev Calculator")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173",
                   "https://jev-calculator-rouge.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class CalculationRequest(BaseModel):
    query: str


@app.get("/")
def home():
    return {
        "message": "Jev Calculator API is running"
    }


@app.post("/calculate")
def calculate_expression(request: CalculationRequest):

    # 1. Let JEV decide which tool to use
    decision = decide_operation(request.query)

    tool_name = decision["decision"]["tool"]
    operation = decision["decision"]["operation"]

    # 2. Handle knowledge queries
    if tool_name == "knowledge":

        try:
            result = execute_tool(
                tool_name=tool_name,
                operation=operation,
                query=request.query
            )

            return {
                "success": True,
                "query": request.query,
                "tool": tool_name,
                "operation": operation,
                "result": result,
                "decision_source": decision["source"]
            }

        except ValueError as e:
            return {
                "success": False,
                "error": str(e)
            }

    # 3. Handle calculator queries
    if tool_name == "calculator":

        if operation is None:
            return {
                "success": False,
                "error": "Could not determine the operation."
            }

        # Extract numbers only for calculator queries
        numbers = extract_numbers(request.query)

        # Square root requires one number
        if operation == "sqrt":

            if len(numbers) != 1:
                return {
                    "success": False,
                    "error": "Square root requires exactly one number."
                }

            a = numbers[0]
            b = None

        # All other calculator operations require two numbers
        else:

            if len(numbers) != 2:
                return {
                    "success": False,
                    "error": "This operation requires exactly two numbers."
                }

            a, b = numbers

        # Execute calculation
        try:

            result = execute_tool(
                tool_name=tool_name,
                operation=operation,
                a=a,
                b=b
            )

        except ValueError as e:

            return {
                "success": False,
                "error": str(e)
            }

        return {
            "success": True,
            "query": request.query,
            "tool": tool_name,
            "operation": operation,
            "a": a,
            "b": b,
            "result": result,
            "decision_source": decision["source"]
        }

    # 4. Unknown tool
    return {
        "success": False,
        "error": f"Unknown tool: {tool_name}"
    }