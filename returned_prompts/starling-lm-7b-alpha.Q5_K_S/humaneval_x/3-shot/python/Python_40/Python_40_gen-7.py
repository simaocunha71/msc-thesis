    def triples_sum_to_zero_helper(l: list, i: int):
        if i == len(l) - 2:
            return l[i] + l[i + 1] + l[-1] == 0

        return triples_sum_to_zero_helper(l, i + 1) or (l[i] + l[i + 1] + l[-1] == 0)

    return triples_sum_to_zero_helper(l, 0)


