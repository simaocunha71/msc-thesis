def combinations_list(lst):
    if not lst:
        return [[]]
    else:
        head = lst[0]
        tail = lst[1:]
        result = combinations_list(tail)
        return result + [[head] + combo for combo in result]


def combinations_list(lst):
    if not lst:
        return [[]]
    else:
        return combinations_list(lst[1:]) + [[lst[0]] + combo for combo in combinations_list(lst[1:])]


def combinations_list(lst):
    if not lst:
        return [[]]
    else:
        head = lst[0]
        tail = lst[1:]
        combinations = combinations_list(tail)
        return [head] + combinations + [combo + [head] for combo in combinations]


def combinations_list(lst):
    if not lst:
        return [[]]
    else:
        return [lst[0]] + combinations_list(lst[1:]) + [[lst[0]] + combo for combo in combinations_list(lst[1:])]


def combinations_list(lst):
    if not lst:
        return [[]]
    else:
        return [lst[0]] + combinations_list(lst[1:]) + [[lst[0]] + combo for combo in combinations_list(lst[1:])]


def combinations_list(lst):
    if not lst:
        return [[]]
    else:
        return [lst[0]] + combinations_list(lst[1:]) + [[lst[0]] + combo for combo in combinations_list(lst[1:])]


def combinations_list(lst):
    if not lst:
        return [[]]
    else:
        return [lst[0]] + combinations_list(lst[1:]) + [[lst[0]] + combo for combo in combinations_list(lst[1:])]


def combinations_list(lst):
    if not lst:
        return [[]]
    else:
        return