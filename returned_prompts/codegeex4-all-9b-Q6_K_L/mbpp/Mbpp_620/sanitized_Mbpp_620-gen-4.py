def largest_subset(numbers):
    """
    Given a list of numbers, find the size of the largest subset where every pair of numbers is divisible by each other.
    """
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def lcm(a, b):
        return a * b // gcd(a, b)

    def is_divisible_pair(a, b):
        return a % b == 0 or b % a == 0

    subset = set()
    for num in numbers:
        if num not in subset:
            subset.add(num)
            for other in subset.copy():
                if not is_divisible_pair(num, other):
                    subset.remove(other)

    return len(subset)