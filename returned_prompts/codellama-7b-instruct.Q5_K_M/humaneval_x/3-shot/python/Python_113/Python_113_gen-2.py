    result = []
    for s in lst:
        count = 0
        for c in s:
            if int(c) % 2 == 1:
                count += 1
        result.append(f"the number of odd elements {count}n the str{count}ng {count} of the {count}nput.")

    return result


