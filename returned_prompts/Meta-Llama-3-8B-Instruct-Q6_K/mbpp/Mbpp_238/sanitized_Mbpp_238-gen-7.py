def number_of_substrings(s):
    return sum(range(len(s) + 1)) - len(s)