"""
def max_sub_array_sum_repeated(arr, k, n):
    # Initialize variables
    max_sum = 0
    current_sum = 0
    
    # Iterate over the array
    for i in range(n):
        # Calculate the sum of the current window
        current_sum += arr[i]
        
        # If the current sum is greater than the max sum
        if current_sum > max_sum:
            # Update the max sum
            max_sum = current_sum
        
        # If the current sum is negative
        if current_sum < 0:
            # Reset the current sum
            current_sum = 0
    
    # Return the max sum
    return max_sum * k
"""
