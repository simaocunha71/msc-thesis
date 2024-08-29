def median_num(lst):
    lst.sort()
    n = len(lst)
    if n % 2 == 0:
        median1 = lst[n//2]
        median2 = lst[n//2 - 1]
        median = (median1 + median2)/2
    else:
        median = lst[n//2]
    return median

print(median_num([10,