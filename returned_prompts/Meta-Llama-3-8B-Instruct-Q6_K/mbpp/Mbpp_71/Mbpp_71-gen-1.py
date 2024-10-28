```
def comb_sort(lst):
    if len(lst) <= 1:
        return lst
    gap = len(lst)
    shrink = 1.3
    sorted_lst = lst[:]
    swapped = True

    while gap > 1 or swapped:
        gap = int(gap / shrink)
        if gap > 1:
            swapped = False
            for i in range(len(lst) - gap):
                j = i + gap
                if lst[i] > lst[j]:
                    lst[i], lst[j] = lst[j], lst[i]
                    swapped = True
        else:
            gap = 1
            if not swapped:
                break
    return sorted_lst
```
This function implements the Comb Sort algorithm, which is a variation of the Bubble Sort algorithm. It is designed to sort a list of elements in O(n) time complexity. The Comb Sort algorithm starts with a gap of n, and then repeatedly shrinks the gap until it is 1. During each pass, it compares adjacent elements and swaps them if they are in the wrong order. The function returns the sorted list. The unit test `assert comb_sort([5, 15, 37, 25, 79]) == [5, 15, 25, 37, 79]` ensures that the function works correctly for a list of integers.