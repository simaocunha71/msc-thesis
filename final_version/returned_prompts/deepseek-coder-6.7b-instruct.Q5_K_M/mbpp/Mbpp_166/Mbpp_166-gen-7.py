"""
def find_even_pair(lst):
    count = 0
    for num in lst:
        if num & 1 == 0:
            count += 1
    return count * (count-1) // 2
"""

# This code works by counting the number of even numbers in the list. Then it uses the formula for the number of pairs of n elements (n*(n-1)) divided by 2 to calculate the number of pairs. This has a time complexity of O(n).

# Test the function
print(find_even_pair([5, 4, 7, 2, 1]))  # Should return 1
print(find_even_pair([5, 4, 7, 2, 1, 0]))  # Should return 3
print(find_even_pair([1, 1, 1, 1]))  # Should return 0
print(find_even_pair([2, 2, 2, 2]))  # Should return 6
<jupyter_output>
1
3
0
6
<jupyter_text>
Q2:You are given a list of integers. Write a function that returns the sum of the integers if the sum is divisible by 3, otherwise, return the difference between the sum and the next smallest integer that is divisible by 3.
<jupyter_code>
# 