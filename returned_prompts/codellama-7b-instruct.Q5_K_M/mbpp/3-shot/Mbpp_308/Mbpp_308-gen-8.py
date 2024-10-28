
def large_product(list1,list2,n):
    list1=sorted(list1,reverse=True)
    list2=sorted(list2,reverse=True)
    result=[]
    for i in range(n):
        result.append(list1[i]*list2[i])
    return result


