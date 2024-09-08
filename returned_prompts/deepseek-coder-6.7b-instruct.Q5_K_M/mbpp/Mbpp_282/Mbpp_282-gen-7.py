def sub_list(l1, l2):
    return [a - b for a, b in zip(l1, l2)]

print(sub_list([1, 2, 3],[4,5,6])) #==[-3,-3,-3]

