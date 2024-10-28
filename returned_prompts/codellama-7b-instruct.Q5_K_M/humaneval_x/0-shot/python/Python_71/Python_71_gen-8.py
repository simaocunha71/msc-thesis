
def triangle_area(a, b, c):
    if a+b>c and b+c>a and c+a>b:
        s = (a+b+c)/2
        return round(s*(s-a)*(s-b)*(s-c),2)
    else:
        return -1
