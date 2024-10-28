def sort_array(arr):
    def count_ones(n):
        return bin(n).count('1')

    return sorted(arr, key=lambda x: (count_ones(x), x))

print sort_array([1, 5, 2, 3, 4])
print sort_array([-2, -3, -4, -5, -6])
print sort_array([1, 0, 2, 3, 4])