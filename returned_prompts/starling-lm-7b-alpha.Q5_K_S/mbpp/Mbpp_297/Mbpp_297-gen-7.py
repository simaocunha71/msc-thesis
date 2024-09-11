def flatten_list(nested_list):
    flat_list = []
    for i in nested_list:
        if isinstance(i, list):
            flat_list.extend(flatten_list(i))
        else:
            flat_list.append(i)
    return flat_list

# assert flatten_list([0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]])==[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
# assert flatten_list([[1, 2], [3, [4, 5]], 6, None]) == [1, 2, 3, 4, 5, 6, None]
# assert flatten_list([]) == []
# assert flatten_list([1]) == [1]
# assert flatten_list([1, 2, 3]) == [1, 2, 3]
# assert flatten_list([1, [2, 3]]) == [1, 2, 3]
# assert flatten_list([1, [2, [3, 4]]]) == [1, 2, 3, 4]

def flatten_list(nested_list):
    flat_list = []
    for i in nested_list:
        if isinstance(i, list):
            flat_list.extend(flatten_list(i))
        else:
            flat_list.append(i)
    return flat_list

# assert flatten_list([0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]])==[0, 10, 20, 30, 40, 50, 60, 70,