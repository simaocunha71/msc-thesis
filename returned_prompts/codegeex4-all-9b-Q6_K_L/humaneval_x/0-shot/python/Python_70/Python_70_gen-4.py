def strange_sort_list(lst):
    '''
    Given list of integers, return list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
    strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    strange_sort_list([]) == []
    '''
    import numpy as np
    lst = np.array(lst)
    sort_lst = np.zeros(len(lst))
    if len(lst) == 0:
        return sort_lst
    else:
        for i in range(0,len(lst)):
            if i%2 == 0:
                sort_lst[i] = min(lst)
                lst[lst == min(lst)] = 0
            else:
                sort_lst[i] = max(lst)
                lst[lst == max(lst)] = 0
        return sort_lst.tolist()