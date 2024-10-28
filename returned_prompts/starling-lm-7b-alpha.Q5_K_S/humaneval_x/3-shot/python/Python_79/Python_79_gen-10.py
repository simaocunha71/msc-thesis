    def to_bin(n):
        if n == 0:
            return '0'
        else:
            return str(n % 2) + to_bin(n // 2)

    return 'db' + to_bin(decimal) + 'db'


