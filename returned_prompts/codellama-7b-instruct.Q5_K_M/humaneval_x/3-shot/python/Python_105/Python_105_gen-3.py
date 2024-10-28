    arr = sorted(arr)
    arr.reverse()
    result = []
    for i in arr:
        if 1 <= i <= 9:
            result.append(str(i))

    return [eval("'{}'".format(x)) for x in result]


