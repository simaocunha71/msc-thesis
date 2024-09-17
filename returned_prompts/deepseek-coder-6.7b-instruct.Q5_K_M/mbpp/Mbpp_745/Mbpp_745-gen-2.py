
def divisible_by_digits(startnum, endnum):
    result = []
    for i in range(startnum, endnum+1):
        if all(i % int(j) == 0 for j in str(i) if j != '0'):
            result.append(i)
    return result


