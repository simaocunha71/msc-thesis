def first_repeated_char(str):
    dict = {}
    for char in str:
        if char in dict:
            return char
        else:
            dict[char] = 1
    return None