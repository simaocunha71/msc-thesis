def count_Pairs(mylist,n):
    count = 0
    for i in range(0,n):
        for j in range(i+1,n):
            if mylist[i] != mylist[j]:
                count = count + 1
    return count