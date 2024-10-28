def sort_array(arr):
    def bin_count(num):
        return bin(num).count('1'), num

    return sorted(arr, key=bin_count)

print(sort_array([1, 5, 2, 3, 4]))
print(sort_array([-2, -3, -4, -5, -6]))
print(sort_array([1, 0, 2, 3, 4]))