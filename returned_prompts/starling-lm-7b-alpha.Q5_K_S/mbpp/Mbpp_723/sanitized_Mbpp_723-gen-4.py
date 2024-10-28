def count_same_pair(list1,list2):
    counter = 0
    for i in range(len(list1)):
        if list1[i] == list2[i]:
            counter += 1
    return counter