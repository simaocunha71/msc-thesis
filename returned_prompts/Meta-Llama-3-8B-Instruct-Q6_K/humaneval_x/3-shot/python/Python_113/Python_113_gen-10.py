    result = []
    for i, s in enumerate(lst, 1):
        count = sum(1 for c in s if int(c) % 2 != 0)
        result.append(f"the number of odd elements {count}n the str{i}ng {i} of the {i}nput.")

    return result


