"""
def large_product(list1,list2,n):
    list1.sort()
    list2.sort()
    list1.reverse()
    list2.reverse()
    i=0
    j=0
    product=[]
    while i<len(list1) and j<len(list2):
        if i==len(list1)-1:
            product.append(list2[j]*list1[i])
            break
        elif j==len(list2)-1:
            product.append(list1[i]*list2[j])
            break
        else:
            if list1[i]<list2[j]:
                product.append(list1[i]*list2[j])
                j+=1
            else:
                product.append(list1[i]*list2[j])
                i+=1
    return product[:n]
"""

# Python program to find largest products from two lists

def large_product(list1,list2,n):
    list1.sort(reverse = True)
    list2.sort(reverse = True)
    while n:
        product = list1.pop(0) * list2.pop(0)
        n -= 1
        yield product


list1 = [1, 2, 3, 4, 5, 6]
list2 = [3, 6, 8, 9, 10, 6]

for x in large_product(list1,list2,3):
    print(x)


# This code is contributed by m_mk
"""




"""




























































































































