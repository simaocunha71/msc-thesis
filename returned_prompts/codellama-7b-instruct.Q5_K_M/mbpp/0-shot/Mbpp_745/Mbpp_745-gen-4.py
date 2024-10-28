def divisible_by_digits(startnum, endnum):
    ans = []
    for i in range(startnum, endnum+1):
        if all(str(i)[j] in str(i) for j in range(len(str(i)))):
            ans.append(i)
    return ans

# 
