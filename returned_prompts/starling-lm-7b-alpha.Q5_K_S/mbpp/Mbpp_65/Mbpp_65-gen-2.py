def recursive_list_sum(lst):
    total = 0
    for elem in lst:
        if isinstance(elem, list):
            total += recursive_list_sum(elem)
        else:
            total += elem
    return total

# assert recursive_list_sum([1, 2, [3,4],[5,6]])==21

def flatten_list(lst):
    return [elem for sublist in lst for elem in sublist]

def recursive_list_sum(lst):
    return sum(flatten_list(lst))

# assert recursive_list_sum([1, 2, [3,4],[5,6]])==21

def recursive_list_sum(lst):
    if isinstance(lst[0], list):
        return recursive_list_sum(lst[0]) + recursive_list_sum(lst[1:])
    else:
        return lst[0] + recursive_list_sum(lst[1:])

# assert recursive_list_sum([1, 2, [3,4],[5,6]])==21

def recursive_list_sum(lst):
    if isinstance(lst, list):
        return sum(recursive_list_sum(elem) for elem in lst)
    else:
        return lst

# assert recursive_list_sum([1, 2, [3,4],[5,6]])==21

def recursive_list_sum(lst):
    if isinstance(lst, list):
        return sum(recursive_list_sum(elem) for elem in lst if isinstance(elem, list))
    else:
        return lst

# assert recursive_list_sum([1, 2, [3,4],[5,6]])==21

def recursive_list_sum(lst):
    return sum(elem for sublist in lst for elem in sublist if isinstance(elem, list))

# assert recursive_list_sum([1, 2, [3,4],[5,6]])==21

def recursive_list_sum