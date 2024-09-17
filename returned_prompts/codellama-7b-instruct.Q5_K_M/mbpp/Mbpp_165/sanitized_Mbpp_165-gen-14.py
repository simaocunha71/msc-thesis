def count_char_position(str1):
    count = 0
    for i in range(len(str1)):
        if str1.lower()[i] == chr(ord('a') + i):
            count += 1
    return count