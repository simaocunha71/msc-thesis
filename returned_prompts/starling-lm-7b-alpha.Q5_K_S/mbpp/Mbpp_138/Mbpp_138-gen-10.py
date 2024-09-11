def is_Sum_Of_Powers_Of_Two(n):
    while(n):
        if n & 1:
            return False
        n >>= 1
    return True

"""
Explanation:
The function checks whether the given number can be represented as sum of non-zero powers of 2 or not. It checks whether the number can be represented as sum of binary numbers or not. For example, if the number is 10, the function will check whether 10 is represented as sum of binary numbers 1000(8) + 0010(2) or not. If the number can't be represented as sum of binary numbers, the function will return False, otherwise it will return True.
"""


# Python3 program to check if a
# given number can be
# represented as sum of
# non-zero powers of 2

# Returns true if x can
# be represented as sum
# of non-zero powers of 2
def is_Sum_Of_Powers_Of_Two(x):

    # Create an array to store
    # result of powers of 2
    two = []
    while (x > 0):
        if (x % 2 == 1):
            two.append(1)
        x = x >> 1

    # If there are no
    # non-zero powers of 2
    if (len(two) == 0):
        return False

    # Iterate through the array
    # to find if there are
    # consecutive 1s
    for i in range(len(two)):
        if (two[i] == 1
            and two[i + 1] == 1):
            return False

    return True

# Driver Code

"""
In the above program, we first calculate the binary representation of the given number using bit shifting operation. Then, we traverse the binary representation of the given number and check whether there are consecutive 1s or not. If there are consecutive 1s, then the given number can't be represented as sum of non-zero powers of 2. Otherwise, the given number can be represented as sum of non-zero powers of 2.
"""

# This code