def move_zero(lst):
    return lst.sort(key=lambda x: x==0)
    # lst.sort(key=lambda x: x==0) sorts the list based on the condition x==0 (if x is zero, it is considered True and it moves to the end)