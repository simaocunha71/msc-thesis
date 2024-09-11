def min_k(data, k):
    # Sorting the list by the second element of the tuple
    data.sort(key=lambda x: x[1])
    # Returning the first k elements
    return data[:k]