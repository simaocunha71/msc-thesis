def check_type(my_tuple):
    # checking if all the elements in the tuple are of the same data type
    return len(set(map(type, my_tuple))) == 1



