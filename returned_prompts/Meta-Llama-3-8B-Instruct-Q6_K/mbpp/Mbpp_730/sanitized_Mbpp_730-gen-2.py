def consecutive_duplicates(lst):
    return [i for i in lst if lst.count(i) == 1] or lst[-1:]  # return the last element if it's the only one left