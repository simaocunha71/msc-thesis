"""
def largest_subset(numbers):
    """
    Given a list of numbers, find the size of the largest subset of a list of numbers so that every pair is divisible.
    """
    # Sort the numbers in ascending order
    numbers.sort()
    
    # Initialize the largest subset size to zero
    largest_subset_size = 0
    
    # Initialize the current subset size to zero
    current_subset_size = 0
    
    # Loop through the numbers
    for i in range(len(numbers)):
        # If the current number is divisible by the number at the end of the subset, then add it to the subset
        if numbers[i] % numbers[-1] == 0:
            current_subset_size += 1
        # Otherwise, if the current number is not divisible by the number at the end of the subset, then start a new subset
        else:
            if current_subset_size > largest_subset_size:
                largest_subset_size = current_subset_size
            current_subset_size = 1
    
    # If the current subset size is greater than the largest subset size, then update the largest subset size
    if current_subset_size > largest_subset_size:
        largest_subset_size = current_subset_size
    
    return largest_subset_size
"""
