
def first_repeated_char(s):
    chars = {}
    for char in s:
        if char in chars:
            return char
        else:
            chars[char] = True
    return None


