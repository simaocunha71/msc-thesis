def number_of_substrings(s):
    return sum(len(list(range(len(s)+1))) for _ in range(len(s)+1))