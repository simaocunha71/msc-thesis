def check_occurences(lst):
    return {tuple(sorted(x)): lst.count(x) for x in lst}