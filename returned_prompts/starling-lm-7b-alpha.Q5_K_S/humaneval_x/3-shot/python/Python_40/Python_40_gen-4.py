    def triples_sum_to_zero_helper(l: list, idx: int, cur_sum: int):
        if cur_sum == 0:
            return True
        if idx >= len(l):
            return False
        if idx == 0:
            return triples_sum_to_zero_helper(l, idx + 1, cur_sum + l[idx])
        return triples_sum_to_zero_helper(l, idx + 1, cur_sum + l[idx]) or triples_sum_to_zero_helper(l, idx + 1, cur_sum - l[idx])

    return triples_sum_to_zero_helper(l, 0, 0)


