from typesafe_sdk import Choice, TypeSafeClient

query = "Calculate 25 times 48"

with TypeSafeClient() as client:

    response = client.system_one(
        state=query,
        questions={
            "operation": Choice(
                instructions="What mathematical operation is the user asking for?",
                criteria={
                    "add": "Addition",
                    "subtract": "Subtraction",
                    "multiply": "Multiplication",
                    "divide": "Division",
                    "percentage_of": "Finding a percentage of a number",
                    "power": "Raising a number to a power, including squared",
                    "sqrt": "Finding a square root",
                    "modulo": "Finding a remainder"
                }
            )
        }
    )

answer = response.answers["operation"]

print("Query:", query)
print("Operation:", answer.choice)
print("Confidence:", answer.confidence)