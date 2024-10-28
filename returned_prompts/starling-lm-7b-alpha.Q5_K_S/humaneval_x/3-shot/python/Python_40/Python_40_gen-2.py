    def triples_sum_to_zero_helper(l: list, idx: int):
        if len(l) < 3:
            return False
        if idx == len(l):
            return False
        if l[idx] + l[idx + 1] + l[idx + 2] == 0:
            return True
        if l[idx] + l[idx + 1] + l[idx + 2] < 0:
            return triples_sum_to_zero_helper(l, idx + 1)
        if l[idx] + l[idx + 1] + l[idx + 2] > 0:
            return triples_sum_to_zero_helper(l, idx + 2)

    return triples_sum_to_zero_helper(sorted(l), 0)


