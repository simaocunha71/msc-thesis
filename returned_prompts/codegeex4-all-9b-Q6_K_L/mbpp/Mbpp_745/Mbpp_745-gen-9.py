def divisible_by_digits(startnum, endnum):
    res = []
    for i in range(startnum, endnum+1):
        temp = i
        while(temp > 0):
            digit = temp % 10
            if digit == 0 or i % digit != 0:
                break
            temp = temp // 10
        else:
            res.append(i)
    return res

