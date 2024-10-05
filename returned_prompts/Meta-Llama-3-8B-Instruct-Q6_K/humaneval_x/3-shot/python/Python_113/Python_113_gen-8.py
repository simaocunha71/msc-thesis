    result = []
    for s in lst:
        count = sum(1 for c in s if int(c) % 2 != 0)
        result.append(f"the number of odd elements {count}n the str{s.count('1')}ng {s.count('1')} of the {s.count('1')}nput.")
    return result


