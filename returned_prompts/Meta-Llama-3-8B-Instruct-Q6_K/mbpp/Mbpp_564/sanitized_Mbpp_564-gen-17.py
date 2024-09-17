def count_Pairs(lst, k):
    lst = list(set(lst))  # remove duplicates
    lst.sort()  # sort the list
    count = 0
    for i in range(len(lst)):
        if i + 1 < len(lst) and lst[i + 1] - lst[i] > 1:  # check if there is a gap of at least 1
            count += 1
    return count