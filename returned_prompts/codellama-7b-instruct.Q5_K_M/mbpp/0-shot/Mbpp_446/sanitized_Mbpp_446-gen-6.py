def count_Occurrence(myTuple,myList):
    count = 0
    for i in myList:
        count += myTuple.count(i)
    return count