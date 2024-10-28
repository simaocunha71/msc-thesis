def sort_array(arr):
    def num_of_ones(num):
        return bin(num).count('1')

    def num_of_ones_and_num(num):
        return bin(num).count('1'), num

    return sorted(arr, key=num_of_ones_and_num)

print(sort_array([1, 5, 2, 3, 4]))
print(sort_array([-2, -3, -4, -5, -6]))
print(sort_array([1, 0, 2, 3, 4]))