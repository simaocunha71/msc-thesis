def next_Perfect_Square(n):
    i = n+1
    while True:
        if int(i**0.5)**2 == i:
            return i
        i += 1