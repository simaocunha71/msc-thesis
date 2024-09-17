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