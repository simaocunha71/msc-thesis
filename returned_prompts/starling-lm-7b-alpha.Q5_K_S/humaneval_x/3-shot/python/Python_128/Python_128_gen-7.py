    if len(arr) == 0:
        return None
    elif len(arr) == 1:
        return abs(arr[0])
    else:
        product = 1
        for elem in arr:
            product *= elem // abs(elem)
        return abs(product) * sum(arr)


