def recursive_list_sum(my_list):
    """
    Flatten a list and sum all of its elements.
    :param my_list:
    :return:
    """
    total = 0
    for element in my_list:
        if isinstance(element, list):
            total += recursive_list_sum(element)
        else:
            total += element
    return total


def list_flatten(list_):
    """
    Flatten a list and sum all of its elements.
    :param list_:
    :return:
    """
    for element in list_:
        if isinstance(element, list):
            yield from list_flatten(element)
        else:
            yield element


def list_sum(list_):
    return sum(list_flatten(list_))


def list_sum_recursive(list_):
    total = 0
    for element in list_:
        if isinstance(element, list):
            total += list_sum_recursive(element)
        else:
            total += element
    return total


def list_sum_recursive_2(list_):
    if not list_:
        return 0
    elif isinstance(list_[0], list):
        return list_sum_recursive_2(list_[0]) + list_sum_recursive_2(list_[1:])
    else:
        return list_[0] + list_sum_recursive_2(list_[1:])


def list_sum_recursive_3(list_):
    if not list_:
        return 0
    elif isinstance(list_[0], list):
        return list_sum_recursive_3(list_[0]) + list_sum_recursive_3(list_[1:])
    else:
        return sum(list_)


def list_sum_recursive_4(list_):
    if not list_:
        return 0
    elif isinstance(list_[0], list):
        return list_sum_recursive_4(list_[0]) + list_sum_rec