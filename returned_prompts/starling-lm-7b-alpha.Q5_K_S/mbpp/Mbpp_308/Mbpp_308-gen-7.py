"""
def large_product(list1,list2,n):
    list1.sort(reverse=True)
    list2.sort(reverse=True)
    list3 = []
    for i in range(len(list1)):
        list3.append(list1[i]*list2[i])
    list3.sort(reverse=True)
    return list3[:n]
"""

