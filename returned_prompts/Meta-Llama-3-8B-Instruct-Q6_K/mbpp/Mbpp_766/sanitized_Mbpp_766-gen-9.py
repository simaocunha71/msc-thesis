def pair_wise(lst):
    return [(x, y) for x, y in zip(lst, lst[1:])] + [(lst[-1],)]