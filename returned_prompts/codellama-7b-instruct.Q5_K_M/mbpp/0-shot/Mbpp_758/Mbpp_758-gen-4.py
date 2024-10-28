def unique_sublists(mylist):
    count = {}
    for sublist in mylist:
        t = tuple(sublist)
        if t not in count:
            count[t] = 0
        count[t] += 1
    return count
