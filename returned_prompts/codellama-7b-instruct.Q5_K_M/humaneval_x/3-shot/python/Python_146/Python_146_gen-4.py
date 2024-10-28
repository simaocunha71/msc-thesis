    count = 0
    for num in nums:
        if num > 10:
            if str(num)[0] == '1' or str(num)[-1] == '1':
                count += 1
    return count


