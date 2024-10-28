def get_max_sum(n):
    # Initialize a list of size n+1 with 0's.
    max_sum = [0] * (n+1)
    
    # Loop from 2 to n+1.
    for i in range(2, n+1):
        # Calculate the maximum sum for i using the formula.
        max_sum[i] = max(max_sum[i//2] + max_sum[i//3] + max_sum[i//4] + max_sum[i//5], i)
    
    # Return the last element in the list which represents the maximum sum for n.
    return max_sum[n]