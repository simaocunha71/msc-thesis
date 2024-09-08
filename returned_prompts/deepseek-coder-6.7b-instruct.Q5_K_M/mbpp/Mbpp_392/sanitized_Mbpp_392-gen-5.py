def get_max_sum(n):
    # Initialize a list to store the maximum sum for each number
    sums = [0]*(n+1)
    
    # Calculate the maximum sum for each number
    for i in range(1, n+1):
        sums[i] = max(sums[i//2]+sums[i//3]+sums[i//4]+sums[i//5], i)
    
    # Return the maximum sum for the given number n
    return sums[n]