
def next_Perfect_Square(n):
    i = n
    while True:
        if int(math.sqrt(i))**2 == i:
            return i
        i += 1


