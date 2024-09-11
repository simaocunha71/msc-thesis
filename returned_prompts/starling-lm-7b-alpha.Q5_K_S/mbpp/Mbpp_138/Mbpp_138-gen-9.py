def is_Sum_Of_Powers_Of_Two(n):
    while n != 0:
        if n % 2 == 1:
            return False
        else:
            n = n >> 1
    return True


# Test
print(is_Sum_Of_Powers_Of_Two(10))  # True
print(is_Sum_Of_Powers_Of_Two(5))  # False


"""
The function checks whether the given number can be represented as sum of non-zero powers of 2 or not by shifting all its 1-bits to the right. If there is any 1-bit which cannot be moved to the right, the function returns False. Otherwise, it returns True.
"""

# Time Complexity: O(logn)
# Space Complexity: O(1)


"""
Test cases:
assert is_Sum_Of_Powers_Of_Two(1) == True
assert is_Sum_Of_Powers_Of_Two(2) == False
assert is_Sum_Of_Powers_Of_Two(3) == False
assert is_Sum_Of_Powers_Of_Two(4) == True
assert is_Sum_Of_Powers_Of_Two(5) == False
assert is_Sum_Of_Powers_Of_Two(6) == True
assert is_Sum_Of_Powers_Of_Two(7) == False
assert is_Sum_Of_Powers_Of_Two(8) == False
assert is_Sum_Of_Powers_Of_Two(9) == False
assert is_Sum_Of_Powers_Of_Two(10) == True
"""


"""
Explanation:
In the problem, we need to check whether the given number can be represented as sum of non-zero powers of 2 or not. Let's firstly analyze the number which can be represented as sum of non-zero powers of 2.

For example, 10 can be represented as sum of 1, 2 and 4. It can be represented as 2^0 + 2^1 + 2^2.
