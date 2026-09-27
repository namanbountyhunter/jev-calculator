from calculator import calculate


tests = [
    ("add", 10, 20),
    ("subtract", 30, 15),
    ("multiply", 12, 8),
    ("divide", 100, 5),
    ("power", 2, 10),
    ("modulo", 17, 5),
    ("sqrt", 144, None),
]


for operation, a, b in tests:

    result = calculate(operation, a, b)

    print(
        f"{operation}: "
        f"{a}, {b} -> {result}"
    )