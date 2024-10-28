```
def Find_Min_Length(list_of_lists):
    min_length = float('inf')
    for lst in list_of_lists:
        if len(lst) < min_length:
            min_length = len(lst)
    return min_length
```


In this problem, we are asked to write a function that finds the length of the smallest list in a list of lists. 

The function should take a list of lists as an argument and return the length of the smallest list.

The unit test provided is `assert Find_Min_Length([[1],[1,2]]) == 1`, which means the function should return 1 when the list of lists is `[[1],[1,2]]`.

Here is the solution:

The function `Find_Min_Length` initializes a variable `min_length` to infinity. Then it iterates over each list in the list of lists. If the length of the current list is less than `min_length`, it updates `min_length` with the length of the current list. Finally, it returns `min_length` which is the length of the smallest list.

The time complexity of this function is O(n), where n is the number of lists in the list of lists, because it iterates over each list once. The space complexity is O(1), because it uses a constant amount of space to store the minimum length. 