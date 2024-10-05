

def sort_even(l: list):
    even_indices_values = sorted([value for index, value in enumerate(l) if index % 2 == 0])
    new_l = [even_indices_values.pop(0) if index % 2 == 0 else value for index, value in enumerate(l)]
    return new_l


print(sort_even([1, 2, 3]))  # [1, 2, 3]
print(sort_even([5, 6, 3, 4]))  # [3, 6, 5, 4]
print(sort_even([10, 11, 12, 13, 14, 15, 16, 17, 18, 19]))  # [10, 16, 11, 13, 14, 18, 12, 15, 17, 19]





