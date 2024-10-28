def max_Abs_Diff(lst):
    max_difference = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            max_difference = max(max_difference, abs(lst[i] - lst[j]))
    return max_difference