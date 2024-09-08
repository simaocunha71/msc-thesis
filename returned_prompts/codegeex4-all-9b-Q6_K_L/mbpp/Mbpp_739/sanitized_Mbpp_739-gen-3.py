def find_Index(n):
    def is_triangular_num(num):
        # A number is triangular if 8*n + 1 is a perfect square
        x = (8 * num + 1) ** 0.5
        return x.is_integer()
    
    index = 0
    while True:
        if len(str(index)) == n:
            if is_triangular_num(index):
                return index
        index += 1