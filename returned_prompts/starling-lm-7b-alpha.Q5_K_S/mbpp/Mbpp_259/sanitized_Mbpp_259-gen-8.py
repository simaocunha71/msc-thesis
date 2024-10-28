from itertools import product
def maximize_elements(tuple1, tuple2):
    tuple_max = []
    for i in product(tuple1, tuple2):
        if i[0] > tuple_max[0][0] and i[1] > tuple_max[0][1]:
            tuple_max[0] = i
        elif i[0] > tuple_max[1][0] and i[1] > tuple_max[1][1]:
            tuple_max[1] = i
        elif i[0] > tuple_max[2][0] and i[1] > tuple_max[2][1]:
            tuple_max[2] = i
        elif i[0] > tuple_max[3][0] and i[1] > tuple_max[3][1]:
            tuple_max[3] = i
    return tuple_max