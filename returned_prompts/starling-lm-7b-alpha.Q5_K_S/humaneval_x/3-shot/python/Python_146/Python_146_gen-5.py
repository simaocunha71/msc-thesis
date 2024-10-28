    count = 0
    for num in nums:
        s = str(num)
        if s[0] in '13579' and s[-1] in '13579' and num > 10:
            count += 1
    return count


