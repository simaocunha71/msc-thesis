def two_unique_nums(nums):
    count_dict = {}
    for num in nums:
        count_dict[num] = count_dict.get(num, 0) + 1
    return [num for num, count in count_dict.items() if count == 1]

print(two_unique_nums([1,2,3,2,3,4,5]))  # [1, 4, 5]

Explanation:
We use a dictionary to count the occurrences of each number in the list. Then we return a list of numbers that appear exactly once in the input list.

This solution has a time complexity of O(n), where n is the total number of elements in all of the input lists, because we need to iterate over all of the elements once.
"""

def two_unique_nums(nums):
    count_dict = {}
    for num in nums:
        count_dict[num] = count_dict.get(num, 0) + 1
    return [num for num, count in count_dict.items() if count == 1]

print(two_unique_nums([1,2,3,2,3,4,5]))  # [1, 4, 5]
<jupyter_output>
[1, 4, 5]
<jupyter_text>
Problem 2
<jupyter_code>
"""
