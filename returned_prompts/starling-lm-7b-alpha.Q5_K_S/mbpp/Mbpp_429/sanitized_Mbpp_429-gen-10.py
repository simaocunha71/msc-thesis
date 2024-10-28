def and_tuples(tup1, tup2):
    tup1_list = list(tup1)
    tup2_list = list(tup2)
    result = []
    for i in range(len(tup1_list)):
        result.append(tup1_list[i] & tup2_list[i])
    return tuple(result)