def bell_number(n):
    # Create an array of size n+1 to store the Bell numbers
    bells = [0] * (n + 1)
    # Set the base case: the Bell number of 0 is 1
    bells[0] = 1
    # Use dynamic programming to calculate the remaining Bell numbers
    for i in range(1, n + 1):
        # For each number, the Bell number is the sum of all the partitions of the previous numbers
        for j in range(i):
            bells[i] += bells[j] * bells[i - j - 1]
    # Return the Bell number of n
    return bells[n]