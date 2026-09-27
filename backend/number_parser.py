import re


def extract_numbers(query):
    # Extract numbers without treating the subtraction operator
    # as part of the second number.
    numbers = re.findall(r"\d+(?:\.\d+)?", query)

    numbers = [float(n) for n in numbers]

    if "squared" in query.lower():
        numbers.append(2.0)

    return numbers