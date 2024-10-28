def find_length(binary_string):
    max_length = 0
    current_length = 0
    for char in binary_string:
        if char == '0':
            current_length += 1
        else:
            max_length = max(max_length, current_length)
            current_length = 0
    return max(max_length, current_length)