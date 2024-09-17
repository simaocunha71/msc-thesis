def recursive_list_sum(lst):
    sum = 0
    for item in lst:
        if isinstance(item, list):
            sum += recursive_list_sum(item)
        else:
            sum += item
    return sum