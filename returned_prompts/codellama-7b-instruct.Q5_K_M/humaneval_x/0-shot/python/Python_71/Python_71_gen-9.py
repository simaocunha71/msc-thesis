
def triangle_area(a, b, c):
    if a + b < c:
        return -1
    if a + c < b:
        return -1
    if b + c < a:
        return -1
    return (a+b+c)/2


























