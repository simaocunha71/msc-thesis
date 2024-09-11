"""
def interleave_lists(list1, list2, list3):
    result = []
    for i in range(len(list1)):
        result.append(list1[i])
        result.append(list2[i])
        result.append(list3[i])
    return result

print(interleave_lists([1,2,3,4,5,6,7],[10,20,30,40,50,60,70],[100,200,300,400,500,600,700]))
"""

def interleave_lists(list1, list2, list3):
    return [x for sublist in zip(list1,list2,list3) for x in sublist]

print(interleave_lists([1,2,3,4,5,6,7],[10,20,30,40,50,60,70],[100,200,300,400,500,600,700]))





# Made By Mostafa_Khaled
# 28th May 2020
```