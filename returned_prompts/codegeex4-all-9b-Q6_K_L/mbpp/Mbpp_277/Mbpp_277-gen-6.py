def dict_filter(dic, n):
    filtered_dic = {k: v for k, v in dic.items() if v >= n}
    return filtered_dic

