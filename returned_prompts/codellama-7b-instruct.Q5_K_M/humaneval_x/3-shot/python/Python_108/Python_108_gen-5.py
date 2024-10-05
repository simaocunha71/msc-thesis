    count = 0

    for num in arr:
        s = 0
        for d in str(abs(num)):
            s += int(d)
        if s > 0:
            count += 1

    return count


