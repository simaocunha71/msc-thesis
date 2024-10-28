    result = 0

    for i, e in enumerate(lst):
        if e % 2 == 0 and i % 2 == 1:
            result += e

    return result

