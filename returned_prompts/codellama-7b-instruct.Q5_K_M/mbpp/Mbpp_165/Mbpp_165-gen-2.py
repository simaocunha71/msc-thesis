"""
def count_char_position(string):
    count = 0
    for char in string:
        if char.lower() == chr(ord('a') + string.find(char)).lower():
            count += 1
    return count
"""
