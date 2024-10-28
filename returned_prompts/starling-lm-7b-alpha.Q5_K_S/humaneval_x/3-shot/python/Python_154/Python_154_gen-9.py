    def rotate(word, n):
        return word[n:] + word[:n]
    def check(a, b):
        for i in range(len(b)):
            if b in a:
                return True
            a = rotate(a, 1)
        return False
    return check(a, b)


