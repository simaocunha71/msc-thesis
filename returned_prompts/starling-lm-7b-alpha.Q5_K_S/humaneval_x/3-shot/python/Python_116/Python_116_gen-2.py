    def count_ones(n):
        result = 0
        while n:
            result += n & 1
            n >>= 1
        return result

    def sort_array_helper(arr):
        return sorted(arr, key=lambda x: (count_ones(x), x))

    if isinstance(arr, list):
        return sort_array_helper(arr)
    else:
        return 'Invalid Input'


