    def binary_count(x):
        return bin(x).count('1')

    return sorted(arr, key=lambda x: (binary_count(x), -x))


