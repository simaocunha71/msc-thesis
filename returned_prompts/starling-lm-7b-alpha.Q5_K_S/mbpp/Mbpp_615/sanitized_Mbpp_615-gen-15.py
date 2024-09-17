def average_tuple(test_tup):
    avg_list = []
    for tup in test_tup:
        avg = sum(tup) / len(tup)
        avg_list.append(avg)
    return avg_list