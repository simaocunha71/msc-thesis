def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # Ensure a is always less than or equal to b
    a, b = sorted((a, b))

    # List comprehension to generate even digits between a and b
    return [x for x in range(a, b + 1) if all(int(digit) % 2 == 0 for digit in str(x))]

# Test cases
print(generate_integers(2, 8))  # [2, 4, 6, 8]
print(generate_integers(8, 2))  # [2, 4, 6, 8]
print(generate_integers(10, 14))  # []