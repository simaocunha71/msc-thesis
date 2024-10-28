def count_same_pair(list1, list2):
    cnt = 0
    for i in range(len(list1)):
        if list1[i] == list2[i]:
            cnt += 1
    return cnt