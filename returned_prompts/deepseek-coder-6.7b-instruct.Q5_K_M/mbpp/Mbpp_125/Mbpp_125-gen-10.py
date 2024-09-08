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

assert find_length("11000010001") == 6
"""
Explanation:
The maximum difference occurs between the strings "110000" and "001" (the substrings where we have 2 zeros and 1 one).
"""

"""
