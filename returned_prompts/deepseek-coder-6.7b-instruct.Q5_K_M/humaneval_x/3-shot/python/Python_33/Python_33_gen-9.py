    divisible_by_three = [value for index, value in enumerate(l) if (index + 1) % 3 == 0]
    divisible_by_three.sort()

    result = list(l)
    for index, value in enumerate(l):
        if (index + 1) % 3 == 0:
            result[index] = divisible_by_three.pop(0)

    return result


