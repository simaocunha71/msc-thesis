def recursive_list_sum(lst: list) -> int:
    total = 0
    for i in lst:
        if isinstance(i, list):
            total += recursive_list_sum(i)
        else:
            total += i
    return total