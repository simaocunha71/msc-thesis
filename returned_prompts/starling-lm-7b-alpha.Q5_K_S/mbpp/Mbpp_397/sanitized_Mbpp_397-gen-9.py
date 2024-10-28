def median_numbers(a,b,c):
    if (a<b and b<c) or (b<a and a<c):
        return b
    elif (c<a and a<b) or (b<c and c<a):
        return a
    else:
        return c