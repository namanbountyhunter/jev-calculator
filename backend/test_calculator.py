from jev_service import decide_operation
from calculator import calculate


def process_query(query, a, b):

    # Step 1: Let Jev decide the operation
    decision = decide_operation(query)

    operation = decision["operation"]

    # Step 2: Validate the decision
    if operation is None:
        return {
            "success": False,
            "error": "Could not determine the operation"
        }

    # Step 3: Execute deterministic calculator code
    result = calculate(operation, a, b)

    return {
        "success": True,
        "operation": operation,
        "a": a,
        "b": b,
        "result": result
    }


if __name__ == "__main__":

    result = process_query(
        "Calculate 25 times 48",
        25,
        48
    )

    print(result)