def next_Perfect_Square(n):
    if n <= 0:
        return "Number must be greater than 0"
    else:
        while True:
            n += 1
            if math.sqrt(n).is_integer():
                return n