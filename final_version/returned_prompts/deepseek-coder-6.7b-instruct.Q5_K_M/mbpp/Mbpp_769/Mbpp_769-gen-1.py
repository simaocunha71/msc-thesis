
def Diff(list1, list2):
    return [i for i in list1 if i not in list2]

print(Diff([10, 15, 20, 25, 30, 35, 40], [25, 40, 35]))


"""
Alternative solution:

def Diff(list1, list2):
    return list(set(list1) - set(list2))

print(Diff([10, 15, 20, 25, 30, 35, 40], [25, 40, 35]))

"""

Both solutions use list comprehension to create a new list from the elements in the first list that are not in the second list. The first solution uses the set() function to convert the lists to sets, which are then subtracted to find the elements that are in the first list but not the second. The alternative solution uses the set() function directly to convert the lists to sets, which are then subtracted. The order of the elements in the result list may vary because sets are unordered in Python.

"""
Alternative solution:

def Diff(list1, list2):
    return [i for i in list1 if i not in list2]

print(Diff([10, 15, 20, 25, 30, 35, 40], [25, 40, 35]))

"""
Both solutions use list comprehension to create a new list from the elements in the first list that are not in the second list. The first solution uses the set() function to convert the lists to sets, which are then subtracted to find the elements that are in the first list but not the second. The alternative solution uses the set() function directly to convert the lists to sets, which are then subtracted. The order of the elements in the result list may vary because sets are unordered in Python.

"""
Alternative solution:

def Diff(list1, list2):
    return [i for i in list1 if i not in list2]

print(Diff([10, 15, 20, 25, 30, 35,