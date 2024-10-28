    result = []
    for s in lst:
        odd_count = sum(int(d) % 2 for d in s)
        result.append(f"the number of odd elements {odd_count}n the str{s[0]}ng {s} of the {s[0]}nput.")
    return result


