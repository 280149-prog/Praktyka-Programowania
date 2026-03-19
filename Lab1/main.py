def add(numbers):

    if not numbers:
        return 0

    if is_dot(numbers):
        raise ValueError("Invalid Format")

    numbers = numbers.replace("\n", ",")
    elements = numbers.split(",")

    total = 0

    for element in elements:
        total += int(element)

    return total


def is_dot(numbers):
    if "." in numbers:
        return True

    return False

