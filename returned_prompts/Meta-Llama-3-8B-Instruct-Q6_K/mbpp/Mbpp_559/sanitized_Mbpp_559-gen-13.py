def max_sub_array_sum(arr, n):
    max_sum = float('-inf')
    current_sum = 0
    start = 0
    end = 0
    temp_start = 0
    
    for i in range(n):
        current_sum += arr[i]
        
        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i
            
        if current_sum < 0:
            current_sum = 0
            temp_start = i + 1
            
    return max_sum