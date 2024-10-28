def find_Index(n):
    def is_triangular_number(num):
        x = (1 + (1 + 8 * num) ** 0.5) / 2
        return x.is_integer()

    def find_triangular_number(digit):
        i = 0
        while True:
            if len(str(i * (i + 1) // 2)) == digit:
                return i * (i + 1) // 2
            i += 1

    return find_triangular_number(n)