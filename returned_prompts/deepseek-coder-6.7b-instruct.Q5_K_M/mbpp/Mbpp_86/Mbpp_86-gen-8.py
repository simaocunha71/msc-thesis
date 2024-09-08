"""
Centered hexagonal numbers are a sequence of numbers where every second number is a hexagonal number.
The formula to generate the nth centered hexagonal number is:
    H(n) = H(n - 1) + 3 * (2*n - 1)
with initial conditions:
    H(1) = 1, H(2) = 7
"""

def centered_hexagonal_number(n):
    if n == 1:
        return 1
    elif n == 2:
        return 7
    else:
        return centered_hexagonal_number(n - 1) + 3 * (2 * n - 1)

print(centered_hexagonal_number(10))
assert centered_hexagonal_number(10) == 271

"""
The time complexity of the above solution is O(n) and the space complexity is O(n) due to the recursive call stack.
"""

# Explanation:
# The function centered_hexagonal_number(n) is used to find the nth centered hexagonal number. 
# The base cases are when n is 1 and 2, the function returns 1 and 7 respectively. 
# For n greater than 2, the function recursively calls itself with n - 1 and adds 3 * (2 * n - 1) to get the nth centered hexagonal number.
# The function uses a recursive approach because it uses the same approach to calculate the nth centered hexagonal number. 
# This is a good example of how to use recursion to solve problems that involve sequences or sequences of sequences.
# The time complexity of this solution is O(n) because it performs n recursive calls. 
# The space complexity is O(n) because of the space required for the recursive call stack.
# The assert statement at the end checks that the result of the function is correct. If the result is correct, no output is produced. 
# If the result is incorrect, an AssertionError is raised.
# This solution assumes that the input will be a positive integer. If the input could be a float or negative, additional error checking would be needed.
# The problem statement is a bit ambiguous as it says to find the nth centered hexagonal number, but also