def Diff(list1, list2):
    return list(set(list1) - set(list2))

print(Diff([10, 15, 20, 25, 30, 35, 40], [25, 40, 35]))

#This function works by converting the lists to sets and subtracting the second set from the first. The difference is a set of elements that are in the first set but not in the second.

#If the order of the elements matters, you can use list comprehension:

def Diff(list1, list2):
    return [item for item in list1 if item not in list2]

print(Diff([10, 15, 20, 25, 30, 35, 40], [25, 40, 35]))

#This will return [10, 20, 30, 15] which is the order of the elements in the first list.

#Note: The order of elements in the output list depends on the order of elements in the first list. The set data structure does not maintain the order of elements.

#If you want to maintain the order of elements, you can use list comprehension with 'if item not in list2' condition:

def Diff(list1, list2):
    return [item for item in list1 if item not in list2]

print(Diff([10, 15, 20, 25, 30, 35, 40], [25, 40, 35]))

#This will return [10, 20, 30, 15] which is the order of the elements in the first list.
<jupyter_output>
[10, 20, 30, 15]
[10, 20, 30, 15]
<jupyter_text>
