
def is_Sum_Of_Powers_Of_Two(n):
    # base case
    if n == 0:
        return False
    if n == 1:
        return True
    # recursive case
    return any(is_Sum_Of_Powers_Of_Two(n - 2**i) for i in range(31))

print(is_Sum_Of_Powers_Of_Two(10))  # True

# This program uses a recursive approach to solve the problem. It checks whether the given number can be represented as sum of non-zero powers of 2. If it can be represented, it returns True, else it returns False.

# This solution has a time complexity of O(log(n)) because it checks for the sum of powers of 2 less than or equal to the given number.

# The space complexity is O(log(n)) as well because of the recursive calls to the function.

# Note: It's important to mention that this solution is not optimized for large numbers. For large numbers, a more optimized solution would be needed.
<jupyter_output>
<empty_output>
<jupyter_text>
