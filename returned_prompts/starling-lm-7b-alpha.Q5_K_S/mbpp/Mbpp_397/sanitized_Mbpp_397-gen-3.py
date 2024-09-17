def median_numbers(a,b,c):
    if a>b:
        if b>c:
            return b
        elif a>c:
            return a
        else:
            return c
    elif a<b:
        if b<c:
            return c
        elif a<c:
            return a
        else:
            return b
    else:
        return a