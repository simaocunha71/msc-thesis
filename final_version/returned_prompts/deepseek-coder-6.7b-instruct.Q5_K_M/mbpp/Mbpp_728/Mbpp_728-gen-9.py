def list_diff(lst1, lst2):
    return [i for i in lst1 if i not in lst2]

print(list_diff([1, 2, 3,