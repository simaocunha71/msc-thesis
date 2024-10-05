
def simplify(x, n):
    numerator_x, denominator_x = map(int, x.split('/'))
    numerator_n, denominator_n = map(int, n.split('/'))

    # Calculate LCM of x and n
    lcm = (numerator_x * denominator_n) / gcd((numerator_x, denominator_x, numerator_n, denominator_n))

    # Check if LCM is a whole number
    if lcm % 1 == 0:
        return True
    else:
        return False

# Time Complexity: O(1)
# Space Complexity: O(1)

# Here's a Python implementation of Euclidean algorithm to calculate GCD of four numbers:
def gcd(*args):
    """Calculate the GCD of multiple numbers using Euclidean algorithm.

    Args:
        *args: Positional arguments of type int

    Returns:
        GCD of all the numbers
    """
    while True:
        for a, b in zip(args, args[1:]):
            if a == 0:
                return b
            r = b % a
            args.remove(b)
            args.append(r)
```