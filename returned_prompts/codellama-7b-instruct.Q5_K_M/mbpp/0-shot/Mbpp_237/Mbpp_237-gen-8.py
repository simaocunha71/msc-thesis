def check_occurences(list_of_tuples):
    return {tup: list_of_tuples.count(tup) for tup in set(list_of_tuples)}


