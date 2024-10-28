def even_position(lst):
    return all(i%2==0 and type(i) == int for i in lst[1::2]) == False