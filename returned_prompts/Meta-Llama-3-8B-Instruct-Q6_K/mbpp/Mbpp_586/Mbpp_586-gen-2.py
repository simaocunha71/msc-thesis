```
def split_Arr(arr,n):
    return arr[n:] + arr[:n]
```
This function takes a list and an integer as input. It then returns a new list where the first n elements are moved to the end of the list. The unit test provided ensures that this function works correctly. 

For example, if the input list is [12,10,5,6,52,36] and n is 2, the output will be [5,6,52,36,12,10]. 

This function uses Python's list slicing feature to achieve this. The expression arr[n:] returns a list that includes all elements from the nth index to the end of the list. The expression arr[:n] returns a list that includes all elements from the beginning of the list up to, but not including, the nth index. By concatenating these two lists using the + operator, the function achieves the desired result. 





