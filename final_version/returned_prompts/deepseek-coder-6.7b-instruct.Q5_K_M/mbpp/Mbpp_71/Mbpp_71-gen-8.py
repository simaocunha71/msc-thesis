def comb_sort(lst):
    gap = len(lst)
    shrink = 1.3
    sorted = False

    while not sorted:
        gap = int(gap / shrink)

        if gap <= 1:
            gap = 1
            sorted = True

        i = 0
        while i + gap < len(lst):
            if lst[i] > lst[i + gap]:
                lst[i], lst[i + gap] = lst[i + gap], lst[i]
            i += 1
    return lst

print(comb_sort([5, 15, 37, 25, 79]))  # [5, 15, 25, 37, 79]

#Sorting/counting_sort.py
"""
