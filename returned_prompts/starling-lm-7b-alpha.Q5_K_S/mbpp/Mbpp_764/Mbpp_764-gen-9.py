
def number_ctr(s):
    return len(set(s)) - sum(map(str.isdigit, s))


