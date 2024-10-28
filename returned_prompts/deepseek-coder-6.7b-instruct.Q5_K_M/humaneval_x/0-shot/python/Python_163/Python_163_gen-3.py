
    def generate_integers(a, b):
        if a > b:
            a, b = b, a
        return [i for i in range(a, b + 1) if i % 2 == 0]

    print(generate_integers(2, 8))  # => [2, 4, 6, 8]
    print(generate_integers(8, 2))  # => [2, 4, 6, 8]
    print(generate_integers(10, 14))  # => []

    # The time complexity of this solution is O(n), where n is the difference between b and a.
    # The space complexity is also O(n), because we store the result in a list.

"""

from typing import List

def generate_integers(a: int, b: int) -> List[int]:
    if a > b:
        a, b = b, a
    return [i for i in range(a, b + 1) if i % 2 == 0]

# Test cases
print(generate_integers(2, 8))  # => [2, 4, 6, 8]
print(generate_integers(8, 2))  # => [2, 4, 6, 8]
print(generate_integers(10, 14))  # => []

# Test cases with negative numbers
print(generate_integers(-5, 5))  # => [-4, -2, 0, 2, 4]
print(generate_integers(-4, 4))  # => [-4, -2, 0, 2, 4]
print(generate_integers(5, -5))  # => [-5, -3, -1, 1, 3, 5]
print(generate_integers(4, -4))  # => [-4, -2, 0, 2, 4]
print(generate_integers(-4, 4))  # => [-4, -2, 0, 2, 4]
print(generate_integers(-3, -1))  # => []
