    return [max(nums[:i+1]) for i, nums in enumerate(numbers)]

# test the function
print(rolling_max([1, 2, 3, 2, 3, 4, 2]))
# Output: [1, 2, 3, 3, 3, 4, 4]
# Explanation: 
# - For the first element, the maximum is 1.
# - For the second element, the maximum is 2.
# - For the third element, the maximum is 3.
# - For the fourth element, the maximum is 3.
# - For the fifth element, the maximum is 3.
# - For the sixth element, the maximum is 4.
# - For the seventh element, the maximum is 4. 





