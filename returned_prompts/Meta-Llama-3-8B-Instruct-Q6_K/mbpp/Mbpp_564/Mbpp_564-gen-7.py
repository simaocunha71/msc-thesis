```
def count_Pairs(lst, k):
    lst = list(set(lst))  # remove duplicates
    lst.sort()  # sort the list
    count = 0
    for i in range(len(lst)):
        if i + 1 < len(lst) and lst[i + 1] - lst[i] > 1:  # check if there is a gap of at least 1
            count += 1
    return count
```





The function works by first removing any duplicate elements from the list and then sorting the list. It then iterates over the list, checking for gaps of at least 1 between each pair of adjacent elements. If a gap of at least 1 is found, it increments the count of pairs. Finally, it returns the count of pairs. The unit test `assert count_Pairs([1,2,1],3) == 2` shows that the function should return 2 for the input `[1,2,1]` with a value of `k` set to `3`.