def first_repeated_char(s: str):
    count = {}
    for char in s:
        if char in count:
            return char
        else:
            count[char] = 1
    return None

