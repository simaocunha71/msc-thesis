def count_Pairs(a,b):
    count=0
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i]!=b[j]:
                count+=1
    return count