    if not arr:
        return None

    prod = 1
    for num in arr:
        prod *= num / abs(num)

    return abs(sum(arr)) * int(prod)