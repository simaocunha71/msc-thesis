    # Initialize the sum to 0
    total_sum = 0
    
    # Iterate over the list
    for i in range(len(lst)):
        # Check if the index is even and the element is odd
        if i % 2 == 0 and lst[i] % 2 != 0:
            # Add the element to the sum
            total_sum += lst[i]
    
    # Return the sum
    return total_sum
