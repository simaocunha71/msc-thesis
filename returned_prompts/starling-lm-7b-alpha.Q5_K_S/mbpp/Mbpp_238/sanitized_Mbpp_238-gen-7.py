def number_of_substrings(string):
    length = len(string)
    n = length * (length + 1) // 2
    return n