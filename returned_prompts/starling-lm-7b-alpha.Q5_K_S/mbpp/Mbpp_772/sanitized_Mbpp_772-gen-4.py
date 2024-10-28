def remove_length(string, k):
    l = string.split(' ')
    res = []
    for i in l:
        if len(i) != k:
            res.append(i)
    return ' '.join(res)