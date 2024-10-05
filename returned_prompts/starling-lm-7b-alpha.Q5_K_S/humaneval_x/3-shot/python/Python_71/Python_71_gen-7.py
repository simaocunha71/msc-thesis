    def area(s1, s2, s3):
        p = (s1 + s2 + s3) / 2
        return (p * (p - s1) * (p - s2) * (p - s3)) ** 0.5

    if a + b <= c or a + c <= b or b + c <= a:
        return -1
    return round(area(a, b, c), 2)


