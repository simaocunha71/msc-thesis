def second_smallest(nums):
    m1, m2 = float('inf'), float('inf')
    for x in nums:
        if x <= m1:
            m1, m2 = x, m1
        elif x < m2:
            m2 = x
    return m2

print(second_smallest([1, 2, -8, -2, 0, -2])) #-2

# Time complexity: O(n)
# Space complexity: O(1)

"""
Explanation:
The function works by initializing two variables, m1 and m2, to infinity.
Then it iterates over the list, and whenever it finds a number less than or equal to m1, it updates m1 and m2.
If it finds a number that is between m1 and m2, it updates m2.
By the end of the list, m2 will be the second smallest number.
"""

# Alternative solution using sorting
def second_smallest_sort(nums):
    nums.sort()
    return nums[1]

print(second_smallest_sort([1, 2, -8, -2, 0, -2])) #-2

# Time complexity: O(n log n)
# Space complexity: O(1)

"""
Explanation:
The function works by sorting the list and then returning the second element in the sorted list, which will be the second smallest number.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Problem 2: Given an unsorted array A of size N of non-negative integers, find a continuous sub-array which adds to a given number S.
<jupyter_code>
# 