
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """

    def is_odd(x):
        return x % 2 == 1

    def get_odd_digits(n):
        return [int(x) for x in str(n) if is_odd(int(x))]

    def multiply(n):
        return reduce(lambda x, y: x * y, n)

    return multiply(get_odd_digits(n))







