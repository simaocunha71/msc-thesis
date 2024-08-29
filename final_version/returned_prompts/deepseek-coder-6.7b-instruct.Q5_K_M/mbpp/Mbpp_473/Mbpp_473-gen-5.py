
def tuple_intersection(tuple_list):
    intersection = set(tuple_list[0])
    for tuples in tuple_list[1:]:
        intersection &= set(tuples)
    return intersection


tuple_list = [(3, 4), (5, 6), (9, 10), (4, 5)]
tuple_list2 = [(5, 4), (3, 4), (6, 5), (9, 11)]
print(tuple_intersection(tuple_list + tuple_list2))  # {(4, 5), (3, 4), (5, 6)}


