def Split(List):
    res = []
    for num in List:
        if num % 2 == 0:
            res.append(num)
    return res