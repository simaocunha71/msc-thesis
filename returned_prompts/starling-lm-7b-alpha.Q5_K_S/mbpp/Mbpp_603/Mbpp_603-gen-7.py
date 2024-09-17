
def get_lucid(n):
    lucids = []
    for i in range(1, n + 1):
        if (str(i).count("4") + str(i).count("7")) == 0:
            lucids.append(i)
    return lucids


