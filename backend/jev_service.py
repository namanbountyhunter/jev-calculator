def decide_operation(user_query: str):

    query = user_query.lower()

    # Percentage
    if "%" in query or "percent" in query or "percentage" in query:
        operation = "percentage_of"

    # Square root
    elif "square root" in query or "sqrt" in query:
        operation = "sqrt"

    # Power
    elif (
        "power" in query
        or "raised to" in query
        or "^" in query
        or "squared" in query
    ):
        operation = "power"

    # Modulo
    elif (
        "modulo" in query
        or "mod" in query
        or "remainder" in query
    ):
        operation = "modulo"

    # Addition
    elif (
        "add" in query
        or "plus" in query
        or "sum" in query
        or "+" in query
    ):
        operation = "add"

    # Subtraction
    elif (
        "subtract" in query
        or "minus" in query
        or "difference" in query
        or "-" in query
    ):
        operation = "subtract"

    # Multiplication
    elif (
        "multiply" in query
        or "times" in query
        or "product" in query
        or "*" in query
        or " x " in query
    ):
        operation = "multiply"

    # Division
    elif (
        "divide" in query
        or "divided" in query
        or "quotient" in query
        or "/" in query
    ):
        operation = "divide"

    # Knowledge
    elif any(
        word in query
        for word in [
            "what is",
            "who is",
            "explain",
            "tell me about",
            "define"
        ]
    ):
        return {
            "decision": {
                "tool": "knowledge",
                "operation": "lookup"
            },
            "confidence": 0.9,
            "source": "mock_jev"
        }

    # Unknown operation
    else:
        operation = None

    return {
        "decision": {
            "tool": "calculator",
            "operation": operation
        },
        "confidence": 1.0 if operation else 0.0,
        "source": "mock_jev"
    }


if __name__ == "__main__":

    tests = [
        "Calculate 25 times 48",
        "Add 10 and 20",
        "Divide 100 by 5",
        "Subtract 15 from 30",
        "Calculate 12 x 8",
        "What is 15% of 200?",
        "What is 20 percent of 500?",
        "square root of 144",
        "2 raised to 10",
        "17 modulo 5",
        "What is Python?",
        "Explain FastAPI",
        "Tell me about Jev"
    ]

    for query in tests:
        print(f"\nQuery: {query}")
        print(decide_operation(query))