    result = []
    for s in lst:
        count = 0
        for c in s:
            if int(c) % 2 != 0:
                count += 1
        result.append(f"the number of odd elements {count}n the str{s} of the {len(lst)}nput.")

    return result


