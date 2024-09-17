def median_trapezium(a,b,c):
    x = (a+b)/2
    y = (b+c)/2
    z = (c+a)/2
    return x if x<=y and x<=z else y if y<=x and y<=z else z