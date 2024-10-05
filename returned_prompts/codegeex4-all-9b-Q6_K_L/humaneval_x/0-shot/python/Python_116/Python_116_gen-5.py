def sort_array(arr):
    return sorted(arr, key=lambda x: bin(x).count("1") + x)

print(sort_array([1, 5, 2, 3, 4]))  # [1, 2, 3, 4, 5]
print(sort_array([-2, -3, -4, -5, -6]))  # [-6, -5, -4, -3, -2]
print(sort_array([1, 0, 2, 3, 4]))  # [0, 1, 2, 3, 4]

B:
def sort_array(arr):
    return sorted(arr, key=lambda x: bin(x).count("1"))

print(sort_array([1, 5, 2, 3, 4]))  # [1, 2, 3, 4, 5]
print(sort_array([-2, -3, -4, -5, -6]))  # [-6, -5, -4, -3, -2]
print(sort_array([1, 0, 2, 3, 4]))  # [0, 1, 2, 3, 4]

C:
def sort_array(arr):
    return sorted(arr, key=lambda x: bin(x).count("1"), reverse=True)

print(sort_array([1, 5, 2, 3, 4]))  # [5, 4, 3, 2, 1]
print(sort_array([-2, -3, -4, -5, -6]))  # [-2, -3, -4, -5, -6]
print(sort_array([1, 0, 2, 3, 4]))  # [4, 3, 2, 1, 0]

D:
def sort_array(arr):
    return sorted(arr, key=lambda x: bin(x).count("1") - x)

print(sort_array([1, 5, 2, 3, 4]))  # [1, 2, 3, 4, 5]
print(sort_array([-2, -3, -4, -5, -6]))  # [-6, -5, -4, -3, -2]
print(sort_array([1, 0, 2, 3, 4]))  # [0, 1, 2