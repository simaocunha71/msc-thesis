def count_Pairs(lst, target):
    count = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] != lst[j] and lst[i] + lst[j] == target:
                count += 1
    return count