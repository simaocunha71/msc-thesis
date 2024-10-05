    def is_substring(a, b):
        return b in a

    def rotate_string(s, n):
        return s[n:] + s[:n]

    for i in range(len(b)):
        if is_substring(a, b):
            return True
        b = rotate_string(b, 1)
    return False


