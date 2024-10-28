    count = 0
    for n in nums:
        s = str(n)
        if s[0] in '13579' and s[-1] in '13579' and n > 10:
            count += 1
    return count


