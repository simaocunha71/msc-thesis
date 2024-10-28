
    def unique_digits(x):
        res = []
        for num in x:
            if not any(int(digit) % 2 == 0 for digit in str(num)):
                res.append(num)
        return sorted(res)

    if __name__ == "__main__":
        import doctest
        doctest.testmod()

The function `unique_digits` works by iterating over each number in the input list `x`. For each number, it converts it to a string and checks if any of the characters (i.e., digits) are even by converting them back to integers and checking if the remainder when divided by 2 is 0. If no even digit is found, the number is appended to `res`. Finally, the function returns `res` sorted in ascending order.
"""

# Solution 2:
"""
