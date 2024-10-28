def count_reverse_pairs(lst):
    reverse_pairs = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] == lst[j][::-1]:
                reverse_pairs += 1
            if lst[j] == lst[i][::-1]:
                reverse_pairs += 1
    return reverse_pairs