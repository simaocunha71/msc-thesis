def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    return sorted([x for x in range(min(a, b), max(a, b)+1) if all(int(digit) % 2 == 0 for digit in str(x))])

print(generate_integers(2, 8))  # [2, 4, 6, 8]
print(generate_integers(8, 2))  # [2, 4, 6, 8]
print(generate_integers(10, 14))  # []

# Note: the range function in Python is inclusive of both endpoints, so we need to add 1 to the second endpoint to ensure we include the last number.