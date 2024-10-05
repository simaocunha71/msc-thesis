    def triples_sum_to_zero_helper(l: list, index: int):
        if index == len(l) - 2:
            return False
        else:
            return any(triples_sum_to_zero_helper(l, index + 1) and l[index] + l[index + 1] + l[index + 2] == 0 for _ in range(index + 2, len(l)))

    return triples_sum_to_zero_helper(l, 0)


