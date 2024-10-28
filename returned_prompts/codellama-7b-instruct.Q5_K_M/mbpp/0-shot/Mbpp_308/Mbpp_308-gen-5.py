def large_product(list1,list2,n):
    list1.sort(reverse=True)
    list2.sort(reverse=True)
    return [list1[i]*list2[i] for i in range(n)]
