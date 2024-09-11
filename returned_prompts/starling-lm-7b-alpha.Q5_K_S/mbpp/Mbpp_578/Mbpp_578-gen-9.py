"""
def interleave_lists(list1,list2,list3):
    list4 = []
    for i in range(len(list1)):
        list4.append(list1[i])
        list4.append(list2[i])
        list4.append(list3[i])
    return list4
"""

def interleave_lists(list1,list2,list3):
    list4 = []
    for i in range(len(list1)):
        list4.extend([list1[i],list2[i],list3[i]])
    return list4


#print(interleave_lists([1,2,3,4,5,6,7],[10,20,30,40,50,60,70],[100,200,300,400,500,600,700]))




"""


