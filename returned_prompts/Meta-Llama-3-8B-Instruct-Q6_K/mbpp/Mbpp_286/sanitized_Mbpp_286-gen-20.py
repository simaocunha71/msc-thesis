def max_sub_array_sum_repeated(arr, k, max_sum):
    # Repeat the array k times
    repeated_arr = arr * k
    
    # Initialize the maximum sum and the current sum
    max_sum = float('-inf')
    current_sum = 0
    
    # Iterate over the repeated array
    for num in repeated_arr:
        # Add the current number to the current sum
        current_sum += num
        
        # If the current sum is greater than the maximum sum, update the maximum sum
        if current_sum > max_sum:
            max_sum = current_sum
        
        # If the current sum is less than 0, reset it to 0
        if current_sum < 0:
            current_sum = 0
    
    # Return the maximum sum
    return max_sum