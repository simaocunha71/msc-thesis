def flatten_list(l):
    # initialize an empty list to store the flattened list
    flattened_list = []

    # iterate through the nested list
    for element in l:
        # if the element is a list, then recursively call the flatten_list function
        if type(element) == list:
            flattened_list.extend(flatten_list(element))
        else:
            flattened_list.append(element)

    return flattened_list


def flatten_list_recursive(l):
    flat_list = []
    for element in l:
        if type(element) == list:
            flat_list.extend(flatten_list_recursive(element))
        else:
            flat_list.append(element)
    return flat_list

print(flatten_list_recursive([0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]))


