def count_same_pair(list1, list2):
    if len(list1) != len(list2):
        raise ValueError("Lists must be of the same length")
    count = 0
    for i in range(len(list1)):
        if list1[i] == list2[i]:
            count += 1
    return count