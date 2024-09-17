def sum_Of_Subarray_Prod(lst):
    # If list is empty, return 0
    if not lst:
        return 0
    # Otherwise, calculate the sum of products of all possible sublists
    else:
        # Initialize sum
        sum_ = 0
        # Iterate through the list, calculating the product of each sublist
        for i in range(len(lst)+1):
            product = 1
            for j in range(i, len(lst)):
                product *= lst[j]
                sum_ += product
        # Return the sum
        return sum_