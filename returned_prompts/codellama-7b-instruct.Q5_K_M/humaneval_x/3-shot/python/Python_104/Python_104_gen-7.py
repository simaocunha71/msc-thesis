    result = []
    for i in x:
        temp = str(i)
        for j in temp:
            if int(j) % 2 == 0:
                break
        else:
            result.append(i)

    return sorted(result)


