    def ones(i):
        return bin(i).count('1')

    return sorted(arr, key=lambda i: (-ones(i), -i))


