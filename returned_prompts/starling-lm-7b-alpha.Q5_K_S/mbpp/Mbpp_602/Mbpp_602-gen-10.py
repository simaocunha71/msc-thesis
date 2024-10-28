
def first_repeated_char(s):
    chars = {}
    for i in s:
        if i in chars:
            return i
        chars[i] = 1
    return None


