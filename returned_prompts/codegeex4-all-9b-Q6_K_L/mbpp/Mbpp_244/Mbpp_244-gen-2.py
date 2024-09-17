def next_Perfect_Square(n):
    i = n+1
    while True:
        if i**0.5 == int(i**0.5):
            return i
        i += 1

