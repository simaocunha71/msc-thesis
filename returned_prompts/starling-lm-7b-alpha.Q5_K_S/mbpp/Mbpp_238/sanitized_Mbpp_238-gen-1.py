def number_of_substrings(s):
    length = len(s)
    # The first substring is the whole string
    num_substrings = length
    # For all other substrings, the length can be any number from 1 to the length of the string
    for i in range(length):
        for j in range(i + 1, length + 1):
            num_substrings += 1
    return num_substrings