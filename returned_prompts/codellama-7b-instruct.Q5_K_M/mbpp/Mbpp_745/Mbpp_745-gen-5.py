def divisible_by_digits(startnum, endnum):
    result=[]
    for i in range(startnum, endnum+1):
        if all(i%int(str(i)[j])==0 for j in range(len(str(i)))):
            result.append(i)
    return result


