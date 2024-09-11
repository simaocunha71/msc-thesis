def dif_Square(n):
    # check all numbers up to sqrt(n)
    for i in range(1, int(math.sqrt(n)) + 1):
        # check if n - i^2 is a perfect square
        if math.sqrt(n - i ** 2) % 1 == 0:
            return True
    return False

# assert dif_Square(5) == True
# print(dif_Square(15))
"""
The given function will return True if the given number can be represented as the difference of two squares, otherwise it will return False.
"""

# Time Complexity : O(sqrt(n))
# Space Complexity : O(1)

# Note: The above solution is not efficient. A better solution would be to use the following code:

def dif_Square(n):
    # check if n is a perfect square
    if n % 2 == 0:
        # if n is even, it can not be represented as the difference of two squares
        return False
    i = 3
    while i * i <= n:
        if (i * i) % 4 == 0 and (n - i * i) % (i * i) == 0:
            # if n is odd and i^2 % 4 == 0 and (n - i^2) % (i^2) == 0, it can be represented as the difference of two squares
            return True
        i += 2
    return False

# assert dif_Square(5) == True
# print(dif_Square(15))
"""
The given function will return True if the given number can be represented as the difference of two squares, otherwise it will return False.

Time Complexity : O(sqrt(n))
Space Complexity : O(1)
"""

# Note: The above solution is efficient and has a time complexity of O(sqrt(n)).

# This solution is based on the following logic:

"""
Let's consider a number n. If n is a perfect square, it cannot be represented as the difference of two squares. If n is odd, it can be represented as the difference of two squares if