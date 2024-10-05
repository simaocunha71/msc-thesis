    count = 0
    for num in nums:
        if num > 10 and num % 10 > 1 and num % 10 < 9:
            count += 1
    return count


