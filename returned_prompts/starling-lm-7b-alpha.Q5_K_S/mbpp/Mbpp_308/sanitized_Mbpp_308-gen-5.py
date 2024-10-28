def large_product(lst1,lst2,num):
    lst1.sort(reverse=True)
    lst2.sort(reverse=True)
    res=[]
    for i in range(num):
        res.append(lst1[i]*lst2[i])
    return res