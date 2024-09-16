def get_equal(my_tuples):
    return all(len(my_tuples[0]) == len(tup) for tup in my_tuples)


