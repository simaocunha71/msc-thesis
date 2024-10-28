    def triples_sum_to_zero_helper(l: list, index: int):
        for i in range(index, len(l)):
            for j in range(i + 1, len(l)):
                if l[index] + l[i] + l[j] == 0:
                    return True
            if triples_sum_to_zero_helper(l, i + 1):
                return True
        return False
    return triples_sum_to_zero_helper(l, 0)


