    def rotate(s):
        return s[1:] + s[:1]

    def check(s, t):
        for i in range(len(t)):
            if s.find(t[i:]) != -1:
                return True
        return False

    while len(b) > 0:
        if check(a, b):
            return True
        b = rotate(b)
    return False



