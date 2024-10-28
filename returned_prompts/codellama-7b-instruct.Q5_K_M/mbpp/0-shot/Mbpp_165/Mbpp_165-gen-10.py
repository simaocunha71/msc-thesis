"""
def count_char_position(input_str):
    count = 0
    for i in range(26):
        count += input_str.lower().count(chr(ord('a') + i))
    return count
"""
