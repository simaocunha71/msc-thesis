def and_tuples(t1, t2):
    t1_list = list(t1)
    t2_list = list(t2)
    zipped_list = zip(t1_list, t2_list)
    zipped_list = list(zipped_list)
    result_list = []
    for i in range(len(zipped_list)):
        result_list.append(zipped_list[i][0] & zipped_list[i][1])
    return tuple(result_list)