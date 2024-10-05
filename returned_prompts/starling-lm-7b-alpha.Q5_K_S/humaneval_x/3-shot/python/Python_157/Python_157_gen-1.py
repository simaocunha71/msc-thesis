    def check(a, b, c):
        return a * a + b * b == c * c
    return (check(a, b, c) or check(b, c, a) or check(c, a, b))


