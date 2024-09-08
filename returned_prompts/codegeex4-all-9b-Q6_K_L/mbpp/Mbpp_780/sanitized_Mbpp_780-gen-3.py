def find_combinations(tuples):
    def helper(index, current_sum, target_sum, result):
        if current_sum == target_sum:
            result.append(tuple(sorted(current_sum)))
            return
        if current_sum > target_sum or index == len(tuples):
            return

        for i in range(index, len(tuples)):
            helper(i + 1, current_sum + tuples[i], target_sum, result)

    result = []
    helper(0, 0, sum(tuples), result)
    return result