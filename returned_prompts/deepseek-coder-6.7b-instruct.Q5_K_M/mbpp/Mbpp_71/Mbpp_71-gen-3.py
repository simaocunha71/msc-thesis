def comb_sort(lst):
    gap = len(lst)
    swapped = True

    while gap != 1 or swapped:
        gap = max(1, int(gap / 1.3))
        swapped = False

        for i in range(len(lst) - gap):
            if lst[i] > lst[i + gap]:
                lst[i], lst[i + gap] = lst[i + gap], lst[i]
                swapped = True

    return lst

print(comb_sort([5, 15, 37, 25, 79]))

"""
Explanation:
Comb sort is a hybrid sorting algorithm, derived from bubble sort and insertion sort, designed to perform well on many kinds of real-world data. The algorithm get its name from the way it combines sublists, which are then partially ordered. The process is repeated until the list is sorted.

The gap size is first determined as the length of the list. The list is then sorted by swapping adjacent items if they are in the wrong order. The gap size is then reduced by a factor of 1.3, and the process is repeated until the gap size is 1.
"""

# Question 2

