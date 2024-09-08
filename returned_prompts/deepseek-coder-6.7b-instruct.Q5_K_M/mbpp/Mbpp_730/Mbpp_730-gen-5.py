def consecutive_duplicates(lst):
    new_lst = []
    for i in range(len(lst)):
        if i == 0 or lst[i] != lst[i-1]:
            new_lst.append(lst[i])
    return new_lst

print(consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4 ]))


"""
