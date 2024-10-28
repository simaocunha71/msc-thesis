    def is_unique(digit):
        return all(int(d) % 2 != 0 for d in str(digit))

    return sorted([x for x in x if is_unique(x)])


