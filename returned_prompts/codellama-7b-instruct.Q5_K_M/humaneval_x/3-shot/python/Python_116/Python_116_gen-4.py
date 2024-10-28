    def to_binary_ones(x):
        return bin(x).count('1')

    def to_binary_decimal(x):
        return int(bin(x), 2)

    return sorted(arr, key=lambda x: (to_binary_ones(x), to_binary_decimal(x)))


