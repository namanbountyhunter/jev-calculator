from number_parser import extract_numbers


tests = [
    "Calculate 25 times 48",
    "Add 10 and 20",
    "Divide 100 by 5",
    "Calculate 12.5 times 4.2",
    "Add -10 and 25",
    "20 squared"
]


for query in tests:

    numbers = extract_numbers(query)

    print(f"Query: {query}")
    print(f"Numbers: {numbers}")
    print()