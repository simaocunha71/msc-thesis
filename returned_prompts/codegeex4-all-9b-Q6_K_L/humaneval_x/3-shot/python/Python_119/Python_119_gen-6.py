    total_open = lst[0].count('(') + lst[1].count('(')
    total_close = lst[0].count(')') + lst[1].count(')')

    if total_open == total_close:
        return 'Yes'
    else:
        return 'No'