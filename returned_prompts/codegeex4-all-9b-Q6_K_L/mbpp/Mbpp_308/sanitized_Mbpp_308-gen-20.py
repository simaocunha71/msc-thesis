def large_product(list1:list,list2:list,n:int):
    product = [list1[i]*list2[i] for i in range(len(list1))]
    return sorted(product,reverse=True)[:n]