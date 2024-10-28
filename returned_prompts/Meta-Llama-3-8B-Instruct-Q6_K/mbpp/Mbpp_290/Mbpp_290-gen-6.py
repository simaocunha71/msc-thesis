def max_length(lst):
    max_len = max(len(sublist) for sublist in lst)
    max_sublist = [sublist for sublist in lst if len(sublist) == max_len][0]
    return max_len, max_sublist

# test
print(max_length([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]))  # Expected output: (3, [13, 15, 17]) 
print(max_length([[0], [1], [2], [3], [4, 5, 6]]))  # Expected output: (3, [4, 5, 6])  # Expected output: (3, [4, 5, 6]) 
print(max_length([[0], [1, 2], [1], [2, 3]]))  # Expected output: (2, [2, 3])  # Expected output: (2, [2, 3])  # Expected output: (2, [2, 3]) 
print(max_length([[0]]))  # Expected output: (1, [0]) 
print(max_length([]))  # Expected output: (0, [])  # Expected output: (0, [])  # Expected output: (0, []) 
print(max_length([[1]]))  # Expected output: (1, [1]) 
print(max_length([[1, 2]]))  # Expected output: (2, [1, 2]) 
print(max_length([[1, 2, 3]]))  # Expected output: (3, [1, 2, 3])  # Expected output: (3, [1, 2, 3])  # Expected output: (3, [1, 2, 3]) 
print(max_length([[1, 2, 3, 4]]))  # Expected output: (4, [1, 2, 3, 4]) 
print(max_length([[1, 2, 3, 4, 5]]))  # Expected output: (5, [1, 2, 3, 4, 5])) 
print(max_length([[1, 2, 3, 4, 5, 6]]))  # Expected output: (6, [1, 2, 3, 