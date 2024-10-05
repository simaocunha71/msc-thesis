    result = []
    while n > 0:
        result.append(n)
        n = next_odd_even(n)

    return result


def next_odd_even(n):
    if n % 2 == 0:
        return n + 1
    else:
        return n + 2


