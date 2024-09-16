def divisible_by_digits(startnum, endnum):
    result = []
    for i in range(startnum, endnum+1):
        for j in str(i):
            if i%int(j) != 0:
                break
        else:
            result.append(i)
    return result