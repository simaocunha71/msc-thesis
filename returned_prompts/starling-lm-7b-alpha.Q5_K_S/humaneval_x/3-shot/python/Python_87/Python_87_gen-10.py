    def helper(x, y):
        if x not in lst:
            return []
        return [(i, lst[i].index(x)) for i in range(len(lst)) if x in lst[i]]

    return sorted(helper(x, y) for y in range(len(lst)))


