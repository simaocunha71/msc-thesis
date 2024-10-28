def is_sublist(lst, sublst):
    for i in range(len(lst)):
        if lst[i:i+len(sublst)] == sublst:
            return True
    return False
    #or
    #return any(lst[i:i+len(sublst)] == sublst for i in range(len(lst)))  # for python 3.5+