def min_k(records, k):
    # Sort the records based on the second element of each tuple
    sorted_records = sorted(records, key=lambda x: x[1])

    # Return the first k elements
    return sorted_records[:k]
records = [('Manjeet', 10), ('Akshat', 4), ('Akash', 2), ('Nikhil', 8)]