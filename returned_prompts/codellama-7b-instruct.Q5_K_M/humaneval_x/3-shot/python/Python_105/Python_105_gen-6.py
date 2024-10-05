    res = []
    if arr == []:
        return res
    for i in range(len(arr)):
        if arr[i] > 0 and arr[i] < 10:
            if arr[i] == 1:
                res.append("One")
            elif arr[i] == 2:
                res.append("Two")
            elif arr[i] == 3:
                res.append("Three")
            elif arr[i] == 4:
                res.append("Four")
            elif arr[i] == 5:
                res.append("Five")
            elif arr[i] == 6:
                res.append("Six")
            elif arr[i] == 7:
                res.append("Seven")
            elif arr[i] == 8:
                res.append("Eight")
            elif arr[i] == 9:
                res.append("Nine")
        else:
            res.append(str(arr[i]))
    res.sort()
    res.reverse()
    return res


