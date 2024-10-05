    divisible_by_3 = sorted([l[i] for i in range(len(l)) if i % 3 == 0])
    result = []
    for i in range(len(l)):
        if i % 3 == 0:
            result.append(divisible_by_3.pop(0))
        else:
            result.append(l[i])
    return result


