    def pairs_sum_to_zero_helper(l, index):
        if index >= len(l):
            return False
        if index == len(l) - 1:
            return l[index] == 0
        if l[index] + l[index + 1] == 0:
            return True
        if l[index] + l[index + 1] < 0:
            return pairs_sum_to_zero_helper(l, index + 2)
        return pairs_sum_to_zero_helper(l, index + 1)

    return pairs_sum_to_zero_helper(l, 0)


