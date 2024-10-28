```
def comb_sort(lst):
    swap = True
    gap = len(lst)
    while gap > 1 or swap:
        gap = max(1, int(gap / 1.3))
        swap = False
        i = 0
        while i + gap < len(lst):
            if lst[i] > lst[i + gap]:
                lst[i], lst[i + gap] = lst[i + gap], lst[i]
                swap = True
            i += 1
    return lst
```
This function implements the Comb Sort algorithm, which is a variation of the Bubble Sort algorithm. The main difference is that Comb Sort uses a gap between elements that decreases by a factor of 1.3 in each iteration, whereas Bubble Sort uses a fixed gap of 1. The function sorts the list in ascending order and returns the sorted list. The unit test `assert comb_sort([5, 15, 37, 25, 79]) == [5, 15, 25, 37, 79]` ensures that the function works correctly.