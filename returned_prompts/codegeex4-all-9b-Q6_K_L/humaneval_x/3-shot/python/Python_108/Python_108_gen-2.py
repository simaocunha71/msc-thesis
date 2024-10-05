    count = 0
    for num in arr:
        digits = [int(d) for d in str(abs(num))]
        if sum(digits) > 0:
            count += 1
    return count

