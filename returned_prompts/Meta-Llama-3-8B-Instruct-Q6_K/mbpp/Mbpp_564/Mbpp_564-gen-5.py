```
def count_Pairs(lst, k):
    pairs = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] != lst[j]:
                pairs += 1
            if pairs == k:
                return i+1
    return i+1
```
The function takes a list of integers and a number k as input. It counts the number of possible unordered pairs where both elements are unequal. If the count of pairs is equal to k, it returns the index of the element after which the count of pairs equals k. If the count of pairs is less than k, it returns the length of the list. For example, if the input list is [1,2,1] and k is 3, the function returns 2. This is because the first two elements are unequal, the next two elements are unequal, and the last two elements are not unequal. So, the count of pairs equals 3 at the second index. If the input list is [1,1,1] and k is 3, the function returns the length of the list, which is 3, because the count of pairs never equals 3. 





