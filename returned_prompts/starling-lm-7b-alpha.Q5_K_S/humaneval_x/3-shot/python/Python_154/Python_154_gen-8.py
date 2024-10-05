    def is_substring(a, b):
        return b in a

    def rotate(s):
        return s[1:] + s[:1]

    while b:
        if is_substring(a, b):
            return True
        b = rotate(b)
    return False


