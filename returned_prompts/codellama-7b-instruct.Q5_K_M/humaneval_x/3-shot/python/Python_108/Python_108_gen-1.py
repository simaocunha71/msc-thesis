    count = 0

    for num in arr:
        if sum(map(lambda x: int(x >= 0), str(num))) > 0:
            count += 1

    return count
