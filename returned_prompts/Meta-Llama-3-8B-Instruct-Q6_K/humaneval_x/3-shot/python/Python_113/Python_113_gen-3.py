    result = []
    for s in lst:
        odd_count = 0
        for c in s:
            if int(c) % 2 != 0:
                odd_count += 1
        result.append(f"the number of odd elements {odd_count}n the str{s} of the {s}nput.")
    return result


