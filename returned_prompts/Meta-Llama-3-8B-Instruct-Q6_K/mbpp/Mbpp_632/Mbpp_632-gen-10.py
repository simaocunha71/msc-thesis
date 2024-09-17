```
def move_zero(lst):
    non_zero_elements = [i for i in lst if i != 0]
    return non_zero_elements + [0] * (len(lst) - len(non_zero_elements))
```


The function `move_zero` takes a list as input and returns a new list where all zeroes are moved to the end. It does this by first creating a new list `non_zero_elements` that contains all elements from the input list that are not zeroes. It then returns this list extended with zeroes until the length of the original list is reached. The unit test `assert move_zero([1,0,2,0,3,4]) == [1,2,3,4,0,0]` ensures that the function works correctly. 
The time complexity of this function is O(n) and the space complexity is also O(n), where n is the number of elements in the input list. This is because we are creating a new list that contains all elements from the input list. If we want to solve this problem in-place (i.e., without creating a new list), we would need to use a different approach, such as iterating over the list and swapping elements that are zeroes with elements that are not zeroes. This would have a time complexity of O(n) but a space complexity of O(1), since we are not using any extra space that scales with the input size. 
Here is the code for the in-place solution:
```
def move_zero_inplace(lst):
    i = 0
    for j in range(len(lst)):
        if lst[j] != 0:
            lst[i], lst[j] = lst[j], lst[i]
            i += 1
    return lst
``` 
This function iterates over the list, and whenever it encounters a non-zero element, it swaps it with the element at the current index `i`. The index `i` is incremented whenever a non-zero element is encountered, so that it points to the next position where a non-zero element should be placed. At the end of the function, all non-zero elements are at the beginning of the list, and all zeroes are at the end. 
This function modifies the original list in-place, so it does not need to return anything. The unit test `assert move_zero_inplace([1,0,2,0,3,4]) == [1,2,3,4,0,0]` ensures that the function works correctly. 
The