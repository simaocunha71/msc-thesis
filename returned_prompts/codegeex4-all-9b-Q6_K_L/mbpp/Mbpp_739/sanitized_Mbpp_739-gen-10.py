def find_Index(n):
    def triangular_number(n):
        return n * (n + 1) // 2

    index = 1
    while len(str(triangular_number(index))) < n:
        index += 1

    return index