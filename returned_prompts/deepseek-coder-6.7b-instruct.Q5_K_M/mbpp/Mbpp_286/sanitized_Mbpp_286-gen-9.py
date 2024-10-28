def max_sub_array_sum_repeated(arr, k):
    n = len(arr)
    
    total_sum = sum(arr)
    
    max_end = max_so_far = min_end = min_so_far = arr[0]
    for i in range(1, n*k):
        max_end = max(arr[i%n], max_end + arr[i%n])
        min_end = min(arr[i%n], min_end + arr[i%n])
        max_so_far = max(max_so_far, max_end)
        min_so_far = min(min_so_far, min_end)
    
    if total_sum == min_so_far:
        return max_so_far
    else:
        return max(max_so_far, total_sum - min_so_far)