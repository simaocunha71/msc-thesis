def dif_Square(n):
    # check all numbers up to sqrt(n)
    for i in range(1, int(math.sqrt(n)) + 1):
        # check if n - i^2 is a perfect square
        if math.sqrt(n - i ** 2) % 1 == 0:
            return True
    return False