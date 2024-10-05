    max_num = -1
    for i in lst:
        if i > 0 and i >= max_num and lst.count(i) >= i:
            max_num = i
    return max_num if max_num > 0 else -1