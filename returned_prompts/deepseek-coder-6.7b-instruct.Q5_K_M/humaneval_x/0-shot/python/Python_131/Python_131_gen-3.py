
    def digits(n):
        digits = [int(d) for d in str(n) if int(d) % 2 == 1]
        if len(digits) == 0:
            return 0
        else:
            product = 1
            for d in digits:
                product *= d
            return product

    print(digits(1))  # 1
    print(digits(4))  # 0
    print(digits(235))  # 15

Explanation:

In this solution, we first convert the integer to a string so we can iterate over its digits. We then create a list of the odd digits using a list comprehension. If no odd digits are found, we return 0. Otherwise, we compute the product of the odd digits and return this value.
"""

# Task 2:
"""
