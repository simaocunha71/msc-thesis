def largest_subset(numbers):
    # Sort the numbers in descending order
    numbers.sort(reverse=True)
    
    # Initialize the largest subset size
    largest_subset_size = 0
    
    # Iterate over the numbers
    for i in range(len(numbers)):
        # Check if the current number is divisible by all previous numbers
        if all(numbers[j] % numbers[i] == 0 for j in range(i)):
            # If it is, update the largest subset size
            largest_subset_size = max(largest_subset_size, i + 1)
    
    return largest_subset_size