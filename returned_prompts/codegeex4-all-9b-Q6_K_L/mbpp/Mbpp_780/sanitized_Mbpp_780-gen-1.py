def find_combinations(lst):
    def helper(lst, target, path, res):
        if target == 0:
            res.append(tuple(sorted(path)))
            return
        if target < 0:
            return
        for i in range(len(lst)):
            helper(lst[i + 1:], target - lst[i][0], path + [lst[i]], res)

    res = []
    lst.sort(key=lambda x: x[0])
    helper(lst, lst[0][0] + lst[0][1], [], res)
    return res