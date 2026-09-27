import math


def calculate(operation: str, a: float, b: float | None = None):

    if operation == "add":
        return a + b

    if operation == "subtract":
        return a - b

    if operation == "multiply":
        return a * b

    if operation == "divide":
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    if operation == "power":
        return a ** b

    if operation == "modulo":
        if b == 0:
            raise ValueError("Cannot calculate modulo by zero")
        return a % b

    if operation == "percentage_of":
        return (a / 100) * b

    if operation == "sqrt":
        if a < 0:
            raise ValueError(
                "Cannot calculate square root of a negative number"
            )
        return math.sqrt(a)

    raise ValueError(f"Unknown operation: {operation}")