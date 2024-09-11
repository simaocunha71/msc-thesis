"""
def comb_sort(list_):
    n = len(list_)
    gap = n + 1
    swapped = True

    while gap != 1 or swapped:
        gap = int(gap / 1.3)
        swapped = False

        for i in range(n - gap):
            if list_[i] > list_[i + gap]:
                list_[i], list_[i + gap] = list_[i + gap], list_[i]
                swapped = True

    return list_

# Test
print(comb_sort([5, 15, 37, 25, 79]))  # [5, 15, 25, 37, 79]
print(comb_sort([37, 15, 25, 5, 79]))  # [5, 15, 25, 37, 79]
print(comb_sort([37, 79, 15, 25, 5]))  # [5, 1