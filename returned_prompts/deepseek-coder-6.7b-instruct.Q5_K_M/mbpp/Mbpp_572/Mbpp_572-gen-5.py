def two_unique_nums(nums: list) -> list:
    return list(set(nums))

print(two_unique_nums([1,2,3,2,3,4,5]))

# output: [1, 2, 3, 4, 5]

# The set() function is used to remove the duplicates from the list.
# The list() function is used to convert the set back into a list.


# If you want to maintain the original order of the list, you can use a different approach:

def two_unique_nums_order(nums: list) -> list:
    unique_nums = []
    for num in nums:
        if num not in unique_nums:
            unique_nums.append(num)
    return unique_nums

print(two_unique_nums_order([1,2,3,2,3,4,5]))

# output: [1, 2, 3, 4, 5]
# In this approach, we iterate over the list and only append the number to the unique_nums list if it's not already there.
# This way, the original order of the list is maintained.
<jupyter_output>
[1, 2, 3, 4, 5]
[1, 2, 3, 4, 5]
<jupyter_text>
Q2
<jupyter_code>
