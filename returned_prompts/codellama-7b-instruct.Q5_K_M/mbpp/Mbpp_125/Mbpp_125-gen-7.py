"""
def find_length(binary_str):
    count = 0
    max_count = 0
    for c in binary_str:
        if c == '1':
            count += 1
            max_count = max(max_count, count)
        else:
            count = 0
    return max_count
"""
