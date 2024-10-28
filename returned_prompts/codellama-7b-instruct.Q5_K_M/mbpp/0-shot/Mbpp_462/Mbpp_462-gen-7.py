
def combinations_list(lst):
    def combinations_list_aux(lst, res, cur):
        if len(lst) == 0:
            res.append(cur)
            return res
        else:
            combinations_list_aux(lst[1:], res, cur)
            combinations_list_aux(lst[1:], res, cur + [lst[0]])
            return res
    return combinations_list_aux(lst, [], [])
