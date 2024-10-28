def perfect_squares(n,m):
    arr = []
    for i in range(n,m+1):
        if i**0.5 == int(i**0.5):
            arr.append(i)
    return arr