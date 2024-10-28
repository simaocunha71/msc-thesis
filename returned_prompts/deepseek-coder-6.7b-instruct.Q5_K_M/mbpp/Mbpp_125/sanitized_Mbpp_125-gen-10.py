def find_length(binary_string: str) -> int:
    max_diff = 0
    current_diff = 0
    for char in binary_string:
        if char == '0':
            current_diff -= 1
        else:
            current_diff += 1
        if current_diff > max_diff:
            max_diff = current_diff
    return max_diff