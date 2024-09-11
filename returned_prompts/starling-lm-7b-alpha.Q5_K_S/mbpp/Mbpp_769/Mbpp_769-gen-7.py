"""
def Diff(list1,list2):
    return [x for x in list1 if x not in list2]
"""

def Diff(list1,list2):
    return list(set(list1)-set(list2))

# print(Diff([10, 15, 20, 25, 30, 35, 40], [25, 40, 35]))





def Diff(list1,list2):
    return [x for x in list1 if x not in list2]

assert Diff([10, 15, 20, 25, 30, 35, 40], [25, 40, 35]) == [10, 20, 30, 15]


# Here is a slightly more efficient approach:
def Diff(list1,list2):
    return list(set(list1) - set(list2))

# print(Diff([10, 15, 20, 25, 30, 35, 40], [25, 40, 35]))





def Diff(list1,list2):
    return [x for x in list1 if x not in list2]

assert Diff([10, 15, 20, 25, 30, 35, 40], [25, 40, 35]) == [10, 20, 30, 15]


# Here is a slightly more efficient approach:
def Diff(list1,list2):
    return list(set(list1) - set(list2))

# print(Diff([10, 15, 20, 25, 30, 35, 40], [25, 40, 35]))





def Diff(list1,list2):
    return [x for x in list1 if x not in list2]

assert Diff([10, 15, 20, 25, 30,