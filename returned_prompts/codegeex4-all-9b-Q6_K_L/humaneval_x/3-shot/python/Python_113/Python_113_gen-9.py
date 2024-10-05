    result = []
    for s in lst:
        odd_count = 0
        for c in s:
            if int(c) % 2 == 1:
                odd_count += 1
        result.append(f"the number of odd elements {odd_count}n the str{odd_count}ng {odd_count} of the {odd_count}nput.")

    return result

