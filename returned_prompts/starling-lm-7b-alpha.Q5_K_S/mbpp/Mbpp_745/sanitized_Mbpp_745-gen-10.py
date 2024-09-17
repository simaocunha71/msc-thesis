def divisible_by_digits(startnum, endnum):
    if startnum==endnum:
        return [startnum] if startnum%(startnum)==0 else []
    if startnum==endnum-1:
        return [startnum,endnum] if startnum%(startnum)==0 and endnum%(endnum)==0 else []
    if startnum>endnum:
        return []
    lst=[startnum]
    if startnum%(startnum)!=0:
        lst.append(startnum+1)
    for i in range(startnum+2,endnum):
        if i%(i)!=0:
            lst.append(i)
    lst.append(endnum)
    return lst if endnum%(endnum)==0 else lst[:-1]
startnum = 1
endnum = 22