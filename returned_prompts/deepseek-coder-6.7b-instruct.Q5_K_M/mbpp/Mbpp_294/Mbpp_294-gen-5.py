def max_val(lst):
    nums = []
    for i in lst:
        if type(i) == int or type(i) == float:
            nums.append(i)
    return max(nums)

print(max_val(['Python', 3, 2, 4, 5, 'version']))

"""
This code takes a list as input, iterates through the list, and checks if each element is an integer or a float. If it is, it adds that element to a new list called nums. After going through the entire list, it returns the maximum value in nums.
"""

"""
