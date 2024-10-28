    result = []
    for s in lst:
        odd_count_in_s = sum(1 for c in s if int(c) % 2 != 0)
        result.append(f"the number of odd elements {odd_count_in_s}n the str{s} of the {s}nput.")
    return result


