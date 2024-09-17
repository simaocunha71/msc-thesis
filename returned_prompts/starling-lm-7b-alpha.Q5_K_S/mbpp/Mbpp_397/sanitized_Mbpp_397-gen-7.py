def median_numbers(a,b,c):
    x = sorted([a,b,c])
    if len(x)%2 == 0:
        return (x[0]+x[1])/2.0
    else:
        return x[1]