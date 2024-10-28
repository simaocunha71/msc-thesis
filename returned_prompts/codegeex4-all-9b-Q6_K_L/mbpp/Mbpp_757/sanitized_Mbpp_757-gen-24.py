def count_reverse_pairs(lst):
    reverse_count = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] == lst[j][::-1]:
                reverse_count += 1
    return reverse_count