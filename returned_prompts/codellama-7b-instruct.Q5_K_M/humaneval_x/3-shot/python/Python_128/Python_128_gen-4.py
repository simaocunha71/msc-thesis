    if not arr:
        return None
    res = 0
    sign = 1
    for x in arr:
        res += abs(x) * sign
        sign *= x // abs(x)
    return res


