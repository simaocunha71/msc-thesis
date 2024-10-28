def combinations_list(lst):
    if not lst:
        return [[]]
    else:
        head = lst[0]
        tail = lst[1:]
        result = combinations_list(tail)
        return result + [[head] + combo for combo in result]