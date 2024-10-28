def sort_counter(dic):
    sorted_dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
    return sorted_dic