    def product(n):
        result = 1
        for c in str(n):
            if int(c) % 2 == 1:
                result *= int(c)
        return result

    if product(n):
        return product(n)
    else:
        return 0


