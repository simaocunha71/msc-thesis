def find_length(binary_string):
    count = 0
    max_count = 0
    for char in binary_string:
        if char == '0':
            count += 1
        else:
            max_count = max(max_count, count)
            count = 0
    return max(max_count, count)