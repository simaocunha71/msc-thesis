def strange_sort_list(lst):
    lst.sort()
    new_lst = []
    for i in range(len(lst)):
        if i % 2 == 0:
            new_lst.append(lst.pop(0))
        else:
            new_lst.append(lst.pop())
    return new_lst

print(strange_sort_list([1, 2, 3, 4]))
print(strange_sort_list([5, 5, 5, 5]))
print(strange_sort_list([]))
