def max_val(list):
    max_val = list[0]
    for i in list:
        if max_val<i:
            max_val = i
    return max_val