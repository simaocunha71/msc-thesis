def max_sub_array_sum(arr, k):
    max_sum = float('-inf')
    current_sum = 0
    left = 0
    
    for right in range(len(arr)):
        current_sum += arr[right]
        
        while current_sum > k and left <= right:
            current_sum -= arr[left]
            left += 1
        
        if current_sum > max_sum:
            max_sum = current_sum
    
    return max_sum