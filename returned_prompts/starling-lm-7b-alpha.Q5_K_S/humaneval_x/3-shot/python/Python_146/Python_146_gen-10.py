    count = 0
    for num in nums:
        first = (num // (10 ** (len(str(num)) - 2))) % 10
        last = num % 10
        if first > 0 and last > 0 and first + last > 10:
            count += 1
    return count


