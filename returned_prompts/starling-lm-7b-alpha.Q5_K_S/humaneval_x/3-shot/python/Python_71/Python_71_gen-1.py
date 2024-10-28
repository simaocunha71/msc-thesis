    def heron(a, b, c):
        s = (a + b + c) / 2
        return (s*(s-a)*(s-b)*(s-c)) ** 0.5
    if not (a + b > c and a + c > b and b + c > a):
        return -1
    return round(heron(a, b, c), 2)


