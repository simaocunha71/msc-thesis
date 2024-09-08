def max_sub_array_sum_repeated(arr, k, n):
    # Calculate the sum of the original array
    total_sum = sum(arr)
    
    # Initialize the maximum sum as negative infinity
    max_sum = float('-inf')
    
    # Iterate through the array k times
    for _ in range(k):
        # Calculate the current sum of the array
        current_sum = sum(arr)
        
        # Update the maximum sum if the current sum is greater
        max_sum = max(max_sum, current_sum)
        
        # Slide the window by one element
        arr = arr[1:] + arr[:1]
    
    return max_sum