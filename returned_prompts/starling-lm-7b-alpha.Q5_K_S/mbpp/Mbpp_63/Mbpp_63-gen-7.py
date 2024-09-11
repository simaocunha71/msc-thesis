"""
def max_difference(tuple_list):
    max_dif = 0
    for i in range(len(tuple_list)):
        for j in range(i+1, len(tuple_list)):
            dif = tuple_