def count_reverse_pairs(lst):
    count = 0
    for i in range(len(lst)):
        if lst[i][::-1] in lst:
            count += 1
    return count//2