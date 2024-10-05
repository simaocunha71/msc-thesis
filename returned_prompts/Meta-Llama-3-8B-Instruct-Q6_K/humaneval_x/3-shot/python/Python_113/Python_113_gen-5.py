    result = []
    for i, s in enumerate(lst, start=1):
        odd_count = sum(int(d) % 2 for d in s)
        result.append(f"the number of odd elements {odd_count}n the str{i}ng {i} of the {i}nput.")

    return result


