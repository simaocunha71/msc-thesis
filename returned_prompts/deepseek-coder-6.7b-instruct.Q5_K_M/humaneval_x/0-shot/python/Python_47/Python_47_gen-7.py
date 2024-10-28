
    l.sort()
    n = len(l)

    if n % 2 == 0:
        median = (l[n//2 - 1] + l[n//2]) / 2
    else:
        median = l[n//2]

    return median

print(median([3, 1, 2, 4, 5]))
print(median([-10, 4, 6, 1000, 10, 20]))


