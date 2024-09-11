def diff_even_odd(list1):
    evenlist = []
    oddlist = []
    for i in list1:
        if i % 2 == 0:
            evenlist.append(i)
        else:
            oddlist.append(i)
    if len(oddlist) > 0 and len(evenlist) > 0:
        return evenlist[0] - oddlist[0]
    else:
        return None


# print(diff_even_odd([1,3,5,7,4,1,6,8]))










"""
def diff_even_odd(list1):
    evenlist = []
    oddlist = []
    for i in list1:
        if i % 2 == 0:
            evenlist.append(i)
        else:
            oddlist.append(i)
    if len(oddlist) > 0 and len(evenlist) > 0:
        return evenlist[0] - oddlist[0]
    else:
        return None
"""

"""
def diff_even_odd(list1):
    evenlist = []
    oddlist = []
    for i in list1:
        if i % 2 == 0:
            evenlist.append(i)
        else:
            oddlist.append(i)
    if evenlist == [] or oddlist == []:
        return None
    else:
        return evenlist[0] - oddlist[0]
"""

"""
def diff_even_odd(list1):
    evenlist = []
    oddlist = []
    for i in list1:
        if i % 2 == 0:
            evenlist.append(i)
        else:
            oddlist.append(i)
    if len(evenlist) == 0 or len(oddlist) == 0:
        return None
    else:
        return evenlist[0] - oddlist[0]
"""

"""
def diff_even_odd(list1):
    evenlist = []
    oddlist = []
    for i in list1:
        if i % 2