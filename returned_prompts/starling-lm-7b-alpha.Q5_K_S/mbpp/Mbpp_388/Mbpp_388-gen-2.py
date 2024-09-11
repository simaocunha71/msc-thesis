def highest_Power_of_2(n):
    if n == 0:
        return 0
    else:
        while (n & (n - 1)):
            n = n & (n - 1)
        return n

# Driver program
print(highest_Power_of_2(10))





"""
The time complexity of the above algorithm is O(1), i.e.,
it runs in constant time regardless of the size of the input.
The space complexity is O(1), i.e., it uses a constant amount of space regardless of the size of the input.

The function works as follows:

Initially, it checks if n is zero, in which case it returns zero as the highest power of 2 is 0 for any n.
If n is nonzero, it enters the while loop and repeatedly performs the bitwise AND operation (n & (n - 1)) until n becomes 0.
In the bitwise AND operation, if both the bits of the operands are 1, then the corresponding position of the result will be set to 1; otherwise, it will be set to 0.
The expression n & (n - 1) effectively clears the rightmost one-bit from n, leaving all the other bits untouched.
The loop continues until n becomes 0, at which point the function returns the value of n, which is the highest power of 2 that is less than or equal to the original value of n.
"""

# Python3 program to find the highest power of 2 that is less than
# or equal to n

# Function to find the highest power of 2 that is less than or equal to n
def highest_Power_of_2(n):
    if n == 0:
        return 0
    else:
        while (n & (n - 1)):
            n = n & (n - 1)
        return n

# Driver program
print(highest_Power_of_2(10))

"""
The time complexity of the above algorithm is O(1), i.e.,
it runs in constant time regardless of the size of the input.
The space complexity is O(1), i.e., it uses a constant amount