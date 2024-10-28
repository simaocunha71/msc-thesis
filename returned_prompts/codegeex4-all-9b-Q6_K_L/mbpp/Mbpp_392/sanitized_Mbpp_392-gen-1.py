def get_max_sum(n):
    # Initialize an array to store maximum sum for each number
    max_sum = [-1] * (n + 1)
    
    # Base cases
    max_sum[0] = 0
    max_sum[1] = 1
    
    # Calculate maximum sum for each number
    for i in range(2, n + 1):
        max_sum[i] = max(i, max_sum[i // 2] + max_sum[i // 3] + max_sum[i // 4] + max_sum[i // 5])
    
    return max_sum[n]