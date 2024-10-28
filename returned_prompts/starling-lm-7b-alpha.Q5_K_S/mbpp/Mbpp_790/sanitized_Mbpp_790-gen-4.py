def even_position(lst):
    if lst[0] % 2 != 0:
        return False
    for i in range(1,len(lst),2):
        if lst[i] % 2 == 0:
            return False
    return True