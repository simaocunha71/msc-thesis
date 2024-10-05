    def to_binary(n):
        if n == 0:
            return '0'
        return to_binary(n // 2) + str(n % 2)

    return to_binary(N)


