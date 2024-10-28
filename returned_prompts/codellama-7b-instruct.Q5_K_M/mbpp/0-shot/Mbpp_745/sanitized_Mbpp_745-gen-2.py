def divisible_by_digits(startnum, endnum):
    result = []
    for i in range(startnum, endnum+1):
        if all(map(lambda x: x==0 or i%x==0, str(i))):
            result.append(i)
    return result