def minSubArraySum(nums):
    min_sum = float('inf')
    current_sum = 0
    
    for num in nums:
        current_sum += num
        
        min_sum = min(min_sum, current_sum)
        
        if current_sum > 0:
            current_sum = 0
            
    return min_sum

# Test the function
print(minSubArraySum([2, 3, 4, 1, 2, 4]))  # Output: 1
print(minSubArraySum([-1, -2, -3]))  # Output: -6

# Explanation:
# We initialize min_sum as positive infinity and current_sum as 0.
# We iterate through the array, adding each number to current_sum.
# We update min_sum with the minimum of min_sum and current_sum.
# If current_sum becomes positive, we reset it to 0.
# Finally, we return min_sum, which is the minimum sum of any non-empty sub-array.