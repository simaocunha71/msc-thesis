    def number_of_ones(n):
        binary = bin(n)[2:]
        return binary.count('1')

    return sorted(arr, key=lambda x: (number_of_ones(x), x))


