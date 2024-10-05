    def get_binary_ones_count(n):
        return bin(n).count('1')

    return sorted(arr, key=lambda x: (get_binary_ones_count(x), x))


