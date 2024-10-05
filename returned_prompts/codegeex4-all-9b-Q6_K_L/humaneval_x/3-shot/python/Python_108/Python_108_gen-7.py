    count = 0
    for num in arr:
        total = 0
        if num < 0:
            num = abs(num)
            total -= 1
        while num:
            total += num % 10
            num //= 10
        if total > 0:
            count += 1
    return count

