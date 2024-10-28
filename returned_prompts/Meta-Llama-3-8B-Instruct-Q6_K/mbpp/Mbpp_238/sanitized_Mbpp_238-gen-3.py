def number_of_substrings(s):
    return sum(len(s) - i for i in range(len(s) + 1)) - len(s)