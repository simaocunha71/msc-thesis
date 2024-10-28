def min_k(tuples, k):
    # Sort the list based on the second element of each tuple
    sorted_tuples = sorted(tuples, key=lambda x: x[1])
    
    # Return the first k elements of the sorted list
    return sorted_tuples[:k]