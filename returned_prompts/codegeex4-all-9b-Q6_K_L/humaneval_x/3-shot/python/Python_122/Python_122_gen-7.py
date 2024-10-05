    total = 0
    count = 0

    for num in arr:
        if count == k:
            break

        if len(str(num)) <= 2:
            total += num

        count += 1

    return total

