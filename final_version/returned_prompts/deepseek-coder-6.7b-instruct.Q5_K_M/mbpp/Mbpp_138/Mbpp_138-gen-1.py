
def is_Sum_Of_Powers_Of_Two(n):
    if n < 1:
        return False
    while n % 2:
        n /= 2
    return n / 2 >= 1

assert is_Sum_Of_Powers_Of_Two(10) == True

"""
Explanation:
We keep dividing the number by 2 until we get a number that is not divisible by 2. This number will be the highest power of 2 that can be subtracted from n. Then we recursively call the function with n-2^power. The base case for the recursion is when n becomes 0, in which case we return True. If we get to a point where n becomes negative, we return False.
"""

"""
Time Complexity: O(log(n))
Space Complexity: O(1)
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Question 2
<jupyter_code>
"""
