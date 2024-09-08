def flatten_list(nested_list):
    flat_list = []
    for i in nested_list:
        if isinstance(i, list):
            for j in i:
                flat_list.append(j)
        else:
            flat_list.append(i)
    return flat_list

print(flatten_list([0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]))

