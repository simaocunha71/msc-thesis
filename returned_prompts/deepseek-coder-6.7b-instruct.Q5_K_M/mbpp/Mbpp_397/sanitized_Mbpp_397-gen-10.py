def median_numbers(a,b,c):
    if (b<a and b>c) or (b>a and b<c):
        return b
    elif (a<b and a>c) or (a>b and a<c):
        return a
    else:
        return c