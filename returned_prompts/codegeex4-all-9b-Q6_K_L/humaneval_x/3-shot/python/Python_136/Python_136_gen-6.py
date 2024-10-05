    if len(lst) == 0:
        return None, None
    elif len(lst) == 1:
        if lst[0] > 0:
            return None, lst[0]
        elif lst[0] < 0:
            return lst[0], None
        else:
            return None, None
    else:
        negatives = [x for x in lst if x < 0]
        positives = [x for x in lst if x > 0]

        if len(negatives) == 0:
            return None, min(positives)
        elif len(positives) == 0:
            return max(negatives), None
        else:
            return max(negatives), min(positives)

