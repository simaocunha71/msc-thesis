def sum_Of_Subarray_Prod(lst):
    def prod(lst):
        p = 1
        for i in lst:
            p *= i
        return p

    return sum(prod(sub) for sub in [lst[i: j] for i in range(len(lst)) for j in range(i + 1, len(lst) + 1)])