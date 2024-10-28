def count_samepair(list1, list2, list3):
    count = 0
    for i in range(max(len(list1), len(list2), len(list3))):
        if i < len(list1) and i < len(list2) and i < len(list3):
            if list1[i] == list2[i] == list3[i]:
                count += 1
    return count