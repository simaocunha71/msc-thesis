def max_val(l):
    ret = l[0]
    for i in l:
        if ret < i:
            ret = i
    return ret