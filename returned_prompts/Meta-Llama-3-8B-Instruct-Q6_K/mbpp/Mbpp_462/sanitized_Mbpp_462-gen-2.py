from itertools import chain, combinations
def combinations_list(input_list):
    return list(chain(*map(lambda x: combinations(input_list, x), range(0, len(input_list)+1))))