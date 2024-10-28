```
def get_pairs_count(lst, sum):
    return len([i for i in range(len(lst)) for j in range(i+1, len(lst)) if lst[i] + lst[j] == sum])
```
This function uses list comprehension to generate all pairs of numbers in the list and then checks if their sum is equal to the given sum. It returns the count of such pairs. The unit test `assert get_pairs_count([1,1,1,1],2) == 6` shows that this function should return 6 when the input list is [1,1,1,1] and the sum is 2, because there are 6 pairs whose sum is 2. For example, (1,1), (1,1), (1,1), (1,1), (1,1), (1,1). 

This function has a time complexity of O(n^2), where n is the length of the input list, because it generates all pairs of numbers in the list. It has a space complexity of O(n), where n is the length of the input list, because it stores all pairs of numbers in the list. 

Note: The function does not consider the order of pairs, i.e., (a, b) is considered the same as (b, a). If you want to consider the order of pairs, you can use a different approach. For example, you can sort the input list and then use two pointers to find the pairs. This approach has a time complexity of O(n log n) and a space complexity of O(1). 