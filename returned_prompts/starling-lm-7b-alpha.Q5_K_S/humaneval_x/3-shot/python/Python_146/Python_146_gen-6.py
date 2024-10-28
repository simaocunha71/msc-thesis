    result = 0
    for num in nums:
        num = str(num)
        if int(num[0]) % 2 != 0 and int(num[-1]) % 2 != 0 and int(num) > 10:
            result += 1
    return result


