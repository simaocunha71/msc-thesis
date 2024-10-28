"""
def find_length(binary_str):
    count = 0
    max_count = 0
    for i in range(len(binary_str)):
        if binary_str[i] == '0':
            count += 1
        else:
            count = 0
        max_count = max(max_count, count)
    return max_count
"""
