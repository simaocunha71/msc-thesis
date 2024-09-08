def find_Index(n):
    def is_triangular_number(num):
        x = (8 * num + 1) ** 0.5
        return x.is_integer()

    index = 1
    while True:
        num = (index * (index + 1)) // 2
        if len(str(num)) == n:
            return index
        index += 1