def number_of_substrings(s):
    if s == "":
        return 0
    else:
        return len(s)*(len(s)+1)//2

