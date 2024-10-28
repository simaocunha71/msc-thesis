def find_char_long(str):
    arr = str.split()
    return [word for word in arr if len(word) >= 4]