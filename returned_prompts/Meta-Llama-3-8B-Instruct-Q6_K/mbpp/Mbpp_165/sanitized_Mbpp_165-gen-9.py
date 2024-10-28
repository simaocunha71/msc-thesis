def count_char_position(s):
    count = 0
    for char in s:
        if char.lower() == chr(ord('a') + ord(char.lower()) - ord('a')):
            count += 1
    return count