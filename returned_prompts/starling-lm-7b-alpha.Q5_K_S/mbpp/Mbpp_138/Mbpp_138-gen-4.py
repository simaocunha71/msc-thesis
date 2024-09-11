def is_Sum_Of_Powers_Of_Two(n):
    return (n > 0) and (bin(n).count('1') == 1)


# Driver code
print(is_Sum_Of_Powers_Of_Two(10))


"""
Given a number, check if it can be represented as a sum of distinct non-zero powers of two. In other words, the number can be represented as 2^i + 2^j + 2^k + ..., where i, j, k, etc. are distinct positive integers.

For example, the number 10 can be represented as a sum of distinct non-zero powers of two because 10 = 2^3 + 2^1. However, the number 11 cannot be represented as a sum of distinct non-zero powers of two because 11 cannot be expressed as a sum of 2^i's.
"""

"""
The given code defines a function `is_Sum_Of_Powers_Of_Two` that takes an integer `n` as input and returns a boolean value indicating whether `n` can be represented as a sum of distinct non-zero powers of two.

The function uses the `bin` function in Python to convert `n` to a binary string. Then, it counts the number of '1' bits in the binary representation of `n` using the `count` method. If the count is equal to 1, it means that `n` can be represented as a sum of distinct non-zero powers of two, so the function returns True. Otherwise, it returns False.

The driver code at the end of the code calls the `is_Sum_Of_Powers_Of_Two` function with the number 10 as an argument and prints the result, which should be True in this case.
"""

"""
To use the given code, you can define your own test cases by modifying the `assert` statement. For example, if you want to check if the number 15 can be represented as a sum of distinct non-zero powers of two, you can use the following code:

assert is_Sum_Of_Powers_Of_Two(15) == True
"""

"""
The time complexity of