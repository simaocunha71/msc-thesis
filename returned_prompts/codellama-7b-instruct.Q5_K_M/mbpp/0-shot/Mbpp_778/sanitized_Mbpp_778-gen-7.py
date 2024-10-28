def pack_consecutive_duplicates(my_list):
    return [[y] + [y for y in my_list if y == x][1:] for x in set(my_list)]