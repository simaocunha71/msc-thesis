    def count_ones(n):
        return bin(n).count("1")

    def compare(a, b):
        if count_ones(a) == count_ones(b):
            return a < b
        else:
            return count_ones(a) < count_ones(b)

    return sorted(arr, cmp=compare)


