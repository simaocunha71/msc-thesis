def catalan_number(n):
    if n<1:
        return 0
    elif n==1:
        return 1
    else:
        return catalan_number(n-1) + catalan_number(n-2) * (2*n-3)