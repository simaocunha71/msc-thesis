def next_Perfect_Square(n):
    if n <= 0:
        return "Invalid input"
    while True:
        n += 1
        if math.sqrt(n) == int(math.sqrt(n)):
            return n