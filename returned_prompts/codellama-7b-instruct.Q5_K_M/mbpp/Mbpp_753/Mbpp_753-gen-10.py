
def min_k(records, k):
    # Sort the records based on the second element of each tuple
    sorted_records = sorted(records, key=lambda x: x[1])

    # Return the first k elements
    return sorted_records[:k]

# Tests

records = [('Manjeet', 10), ('Akshat', 4), ('Akash', 2), ('Nikhil', 8)]
assert min_k(records, 2) == [('Akash', 2), ('Akshat', 4)]

records = [('Manjeet', 10), ('Akshat', 4), ('Akash', 2), ('Nikhil', 8), ('Nitin', 2)]
assert min_k(records, 3) == [('Akash', 2), ('Akshat', 4), ('Nitin', 2)]

records = [('Manjeet', 10), ('Akshat', 4), ('Akash', 2), ('Nikhil', 8), ('Nitin', 2), ('Nilesh', 3), ('Nitin', 1)]
assert min_k(records, 4) == [('Akash', 2), ('Akshat', 4), ('Nilesh', 3), ('Nitin', 1)]

records = [('Manjeet', 10), ('Akshat', 4), ('Akash', 2), ('Nikhil', 8), ('Nitin', 2), ('Nilesh', 3), ('Nitin', 1), ('Nilesh', 5)]
assert min_k(records, 5) == [('Akash', 2), ('Akshat', 4), ('Nilesh', 3), ('Nitin', 1), ('Nilesh', 5)]

records = [('Manjeet', 10), ('Akshat', 4), ('Akash', 2), ('Nikhil', 8), ('Nitin', 