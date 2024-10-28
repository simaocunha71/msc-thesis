    def get_num_ones(n):
        return bin(n).count('1')

    def get_num_bits(n):
        return len(bin(n)) - 2

    return sorted(arr, key=lambda x: (-get_num_ones(x), get_num_bits(x)))


