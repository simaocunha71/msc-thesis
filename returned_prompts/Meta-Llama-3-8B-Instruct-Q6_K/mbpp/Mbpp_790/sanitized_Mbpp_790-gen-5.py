def even_position(lst):
    return all(i%2==0 and isinstance(i, int) and i%2==0 for i in lst[1::2])  # start from 1, end at the end of the list, increment by 2