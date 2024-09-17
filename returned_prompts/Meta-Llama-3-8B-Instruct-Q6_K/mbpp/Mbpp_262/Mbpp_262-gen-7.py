```
def split_two_parts(lst, L):
    return (lst[:L], lst[L:])
```





The function takes a list and an integer L as input, and returns a tuple containing two lists. The first list is a slice of the input list up to the index L, and the second list is the remaining part of the input list starting from index L. 

For example, if the input list is [1,1,2,3,4,4,5,1] and L is 3, the function will return ([1, 1, 2], [3, 4, 4, 5, 1]). 

The unit test `assert split_two_parts([1,1,2,3,4,4,5,1],3)==([1, 1, 2], [3, 4, 4, 5, 1])` ensures that the function behaves as expected. 

The function works by using Python's list slicing feature. The expression `lst[:L]` returns a slice of the list from the beginning up to the index L, and the expression `lst[L:]` returns a slice of the list from index L to the end. The function then returns a tuple containing these two slices. 

This solution has a time complexity of O(n) where n is the length of the input list, because it needs to iterate over the list to create the slices. The space complexity is O(n) as well, because it needs to create two new lists. 

However, note that the function does not handle the case where L is larger than the length of the input list. In this case, the function will return a tuple with two lists: the first list will be the entire input list, and the second list will be an empty list. This is because the expression `lst[L:]` returns an empty list when L is larger than the length of the input list. If you want to handle this case differently, you will need to add additional code to the function. 





```
def split_two_parts(lst, L):
    return (lst[:L], lst[L:])
```





The function takes a list and an integer L as input, and returns a tuple containing two lists. The first list is a slice of the input list up to the index L, and the second list is the remaining part of the input list starting from index L. 

For example, if the input list is [1,1,2