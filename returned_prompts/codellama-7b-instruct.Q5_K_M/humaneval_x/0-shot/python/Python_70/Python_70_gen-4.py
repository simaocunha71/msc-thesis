
def strange_sort_list(lst):
    lst = sorted(lst)
    result = []
    for i in range(len(lst)):
        result.append(lst[i])
        result.append(lst[-i-1])
    return result


