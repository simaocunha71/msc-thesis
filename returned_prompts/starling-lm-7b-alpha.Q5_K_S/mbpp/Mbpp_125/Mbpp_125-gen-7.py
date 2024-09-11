"""
def find_length(binary_str):
    max_len = 0
    for i in range(len(binary_str)):
        count_zeros = 0
        for j in range(i, len(binary_str)):
            if binary_str[j] == '0':
                count_zeros += 1
            else:
                max_len = max(max_len, count_zeros)
                count_zeros = 0
        max_len = max(max_len, count_zeros)
    return max_len
"""

# This solution is wrong
def find_length(binary_str):
    max_len = 0
    for i in range(len(binary_str)):
        count_zeros = 0
        for j in range(i, len(binary_str)):
            if binary_str[j] == '0':
                count_zeros += 1
            else:
                max_len = max(max_len, count_zeros)
                count_zeros = 0
        max_len = max(max_len, count_zeros)
    return max_len

def find_length(binary_str):
    max_len = 0
    for i in range(len(binary_str)):
        count_zeros = 0
        for j in range(i, len(binary_str)):
            if binary_str[j] == '0':
                count_zeros += 1
            else:
                max_len = max(max_len, count_zeros)
                count_zeros = 0
        max_len = max(max_len, count_zeros)
    return max_len

# This solution is wrong
def find_length(binary_str):
    max_len = 0
    for i in range(len(binary_str)):
        count_zeros = 0
        for j in range(i, len(binary_str)):
            if binary_str[j] == '0':
                count_zeros += 1
            else:
                max_len = max(max_len,