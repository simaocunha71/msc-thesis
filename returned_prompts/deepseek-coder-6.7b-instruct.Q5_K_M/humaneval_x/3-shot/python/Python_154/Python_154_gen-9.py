    def rotate(s):
        return s[-1] + s[:-1]

    for _ in range(len(b)):
        if b in a:
            return True
        b = rotate(b)

    return False


