    if len(set(lst)) != len(lst):
        return False

    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False

    return True
# or
    for i in range(len(lst) - 1):
        if lst[i] >= lst[i + 1]:
            return False

    return True
# or
    return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))  # Python 3.5+
# or
    return all(lst[i] < lst[i + 1] for i in range(len(lst) - 1))  # Python 3.5+
# or
    return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1)) or all(lst[i] == lst[i + 1] for i in range(len(lst) - 1))  # Python 3.5+
# or
    return all(lst[i] < lst[i + 1] for i in range(len(lst) - 1)) or all(lst[i] == lst[i + 1] for i in range(len(lst) - 1))  # Python 3.5+


