    count = 0
    for num in arr:
        if sum(map(lambda x: x if x >= 0 else -1, str(num))) > 0:
            count += 1
    return count


