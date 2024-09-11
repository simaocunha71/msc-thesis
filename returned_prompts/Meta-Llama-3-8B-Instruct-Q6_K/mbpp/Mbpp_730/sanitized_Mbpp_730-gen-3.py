def consecutive_duplicates(lst):
    return [i for i in lst if i not in lst[:lst.index(i)] + lst[lst.index(i)+1:]]