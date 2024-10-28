def replace_list(list1, list2):
    list1[-1] = list2
    return list1

# Tests
list1 = [1, 3, 5, 7, 9, 10]
list2 = [2, 4, 6, 8]

assert replace_list(list1, list2)==[1, 3, 5, 7, 9, 2, 4, 6, 8]


