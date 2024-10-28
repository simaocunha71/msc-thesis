def sort_array(arr):
    def count_ones(n):
        return bin(n).count('1')

    def sort_key(n):
        return count_ones(n), n

    return sorted(arr, key=sort_key)

print(sort_array([1, 5, 2, 3, 4]))  # [1, 2, 3, 4, 5]
print(sort_array([-2, -3, -4, -5, -6]))  # [-6, -5, -4, -3, -2]
print(sort_array([1, 0, 2, 3, 4]))  # [0, 1, 2, 3, 4]