def find_combinations(lst):
    if not lst:
        return []
    else:
        first, rest = lst[0], lst[1:]
        pairs = [(first[0]+x[0], first[1]+x[1]) for x in find_combinations(rest)]
        if first in pairs:
            pairs.remove(first)
        return pairs + find_combinations(rest)