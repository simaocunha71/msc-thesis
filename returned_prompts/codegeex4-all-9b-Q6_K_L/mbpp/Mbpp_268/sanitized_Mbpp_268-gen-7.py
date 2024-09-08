def find_star_num(n):
    def factorial(x):
        if x == 0:
            return 1
        else:
            return x * factorial(x-1)
    return n * factorial(n + 1)