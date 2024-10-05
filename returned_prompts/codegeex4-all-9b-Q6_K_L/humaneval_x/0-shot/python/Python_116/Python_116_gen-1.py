def sort_array(arr):
    def sort_key(x):
        return bin(x).count('1'), x
    return sorted(arr, key=sort_key)

print sort_array([1, 5, 2, 3, 4])
print sort_array([-2, -3, -4, -5, -6])
print sort_array([1, 0, 2, 3, 4])
print sort_array([1, 5, 2, 3, 4, 0])

def sort_array(arr):
    def sort_key(x):
        return bin(x).count('1'), x
    return sorted(arr, key=sort_key)

print sort_array([1, 5, 2, 3, 4])
print sort_array([-2, -3, -4, -5, -6])
print sort_array([1, 0, 2, 3, 4])
print sort_array([1, 5, 2, 3, 4, 0])