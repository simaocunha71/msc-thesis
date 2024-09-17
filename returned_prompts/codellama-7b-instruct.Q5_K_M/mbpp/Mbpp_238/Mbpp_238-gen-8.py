
def number_of_substrings(s):
    return sum(1 for i in range(len(s)+1) for j in range(i+1))


