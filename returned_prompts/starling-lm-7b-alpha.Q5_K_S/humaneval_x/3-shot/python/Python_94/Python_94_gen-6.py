    from itertools import chain

    lst = list(chain(*map(lambda x: map(int, str(x).split(','))[:-1], lst)))
    max_lst = max(lst)
    if max_lst > 9999:
        max_lst = int(str(max_lst)[-5:])
    else:
        max_lst = max_lst % 10
    return max_lst


