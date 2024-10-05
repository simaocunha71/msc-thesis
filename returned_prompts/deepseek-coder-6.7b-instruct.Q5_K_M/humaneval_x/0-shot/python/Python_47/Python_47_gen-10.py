
    l.sort()
    if len(l) % 2 == 0:
        median = (l[len(l)//2] + l[len(l)//2 - 1]) / 2
    else:
        median = l[len(l)//2]
    return median


print(median([3, 1, 2, 4, 5]))
print(median([-10, 4, 6, 1000, 10, 20]))
"""

