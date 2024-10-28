    def binary_count(n):
        return bin(n).count('1')

    return sorted(arr, key=lambda x: (binary_count(x), -x))


