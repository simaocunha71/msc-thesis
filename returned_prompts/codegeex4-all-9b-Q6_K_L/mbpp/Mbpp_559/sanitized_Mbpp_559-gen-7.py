def max_sub_array_sum(nums, k):
    # Initialize the maximum sum to be negative infinity
    max_sum = float('-inf')
    
    # Iterate over all possible sublists of length k
    for i in range(len(nums) - k + 1):
        # Calculate the sum of the current sublist
        current_sum = sum(nums[i:i+k])
        
        # Update the maximum sum if the current sum is greater
        max_sum = max(max_sum, current_sum)
    
    return max_sum