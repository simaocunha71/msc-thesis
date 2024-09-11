from itertools import combinations
def find_combinations(tuple_list):
    # flatten the list of tuples
    flat_list = [item for sublist in tuple_list for item in sublist]
    # get the combinations of sums
    combs = list(combinations(flat_list, 2))
    # convert the combinations of tuples back to tuples
    return [(sum(tup1), sum(tup2)) for tup1, tup2 in combs]