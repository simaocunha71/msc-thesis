    def to_bin(n):
        if n == 0:
            return '0'
        else:
            return to_bin(n // 2) + str(n % 2)

    return to_bin(N)


