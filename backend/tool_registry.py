from calculator import calculate
from knowledge_tool import knowledge_tool



TOOLS = {
    "calculator": calculate,
    "knowledge": knowledge_tool
}


def execute_tool(tool_name, operation, a=None, b=None, query=None):
    if tool_name not in TOOLS:
        raise ValueError(f"Unknown tool: {tool_name}")

    tool = TOOLS[tool_name]

    if tool_name == "calculator":
        return tool(operation, a, b)

    if tool_name == "knowledge":
        return tool(query)