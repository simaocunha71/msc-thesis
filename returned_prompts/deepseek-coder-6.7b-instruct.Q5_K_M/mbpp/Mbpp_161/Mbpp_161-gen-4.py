def remove_elements(lst, remove_lst):
    return [i for i in lst if i not in remove_lst]

print(remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8]))


