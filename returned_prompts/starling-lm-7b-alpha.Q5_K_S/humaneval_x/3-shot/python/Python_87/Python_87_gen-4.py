    def helper(lst, x):
        result = []
        for i, row in enumerate(lst):
            if x in row:
                result.append((i, row.index(x)))
        return sorted(result)
    return helper(lst, x)


