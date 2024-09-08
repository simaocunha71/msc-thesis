def find_combinations(tuples):
    def helper(tuples, target, path, result):
        if target == 0:
            result.append(path)
            return
        if target < 0:
            return
        for i in range(len(tuples)):
            helper(tuples[i+1:], target - tuples[i][0], path + [tuples[i]], result)

    result = []
    helper(tuples, 0, [], result)
    return result