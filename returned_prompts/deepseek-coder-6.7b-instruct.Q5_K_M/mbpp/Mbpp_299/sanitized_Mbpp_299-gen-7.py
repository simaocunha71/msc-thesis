def max_aggregate(lst):
    dic = {}
    for name, val in lst:
        if name in dic:
            dic[name] += val
        else:
            dic[name] = val
    max_val = max(dic.values())
    max_name = [k for k, v in dic.items() if v == max_val]
    return (max_name[0], max_val)