    def binary_cnt(n):
        return bin(n).count("1")

    def sort_by_count(a, b):
        return binary_cnt(a) == binary_cnt(b) and a < b or binary_cnt(a) < binary_cnt(b)

    return sorted(arr, key=lambda x: (binary_cnt(x), -x))


