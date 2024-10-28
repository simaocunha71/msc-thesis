    count = 0

    for num in arr:
        total = 0

        while num != 0:
            total += num % 10
            num //= 10

        if total > 0:
            count += 1

    return count

