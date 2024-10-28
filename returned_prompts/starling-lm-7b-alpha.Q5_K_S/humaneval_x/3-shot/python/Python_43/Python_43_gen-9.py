    def pairs_sum_to_zero_helper(l, index, result):
        if index == len(l)-1:
            return result
        if l[index] == 0:
            return True
        if l[index] + l[index+1] == 0:
            return True
        return pairs_sum_to_zero_helper(l, index+1, result)

    return pairs_sum_to_zero_helper(l, 0, False)


