def number_of_substrings(string):
    length = len(string)
    substrings = 0
    for i in range(length):
        for j in range(i + 1, length + 1):
            substrings += 1
    return substrings