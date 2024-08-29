def round_and_sum(nums):
    rounded_nums = [round(num) for num in nums]
    return sum(rounded_nums) * len(nums)

print(round_and_sum([22.4, 4.0, -16.22, -9.10, 11.00, -12.22, 14.20, -5.20, 17.50]))

# Output: 243
<jupyter_output>
243
<jupyter_text>
Problem 3:  Write a Python function to find the maximum sum of a sublist in a given list of integers. The sublist should not have any negative numbers.
<jupyter_code>
