    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    return len(set(lst)) == len(lst)  # check for no duplicate numbers


