
    return "".join(x for x in s if x not in c), all(x == x[::-1] for x in "".join(x for x in s if x not in c))

