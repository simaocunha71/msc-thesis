    product = 1
    for elem in arr:
        product *= (elem > 0) - (elem < 0)

    if len(arr) == 0:
        return None
    else:
        return product * sum(map(abs, arr))


