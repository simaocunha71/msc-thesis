def max_length(lst):
    max_len = 0
    max_list = []
    for sub_list in lst:
        if len(sub_list) > max_len:
            max_len = len(sub_list)
            max_list = sub_list
    return max_len, max_list

# Test case
print(max_length([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]))  # Expected output: (3, [13, 15, 17])

