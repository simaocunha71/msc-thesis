```
def left_insertion(lst, val):
    for i in range(len(lst)):
        if lst[i] >= val:
            return i
    return len(lst)
``` 
The function `left_insertion` takes a sorted list `lst` and a value `val` as input, and returns the index where the value should be inserted to maintain the sorted order. If the value is larger than all elements in the list, the function returns the length of the list.

This function works by iterating over the list, comparing each element with the value, and returning the index where the value should be inserted. The function stops iterating when it finds an element that is greater than or equal to the value.

For example, if the list is `[1,2,4,5]` and the value is `6`, the function will return `4`, which is the index where `6` should be inserted to maintain the sorted order.

The unit test `assert left_insertion([1,2,4,5],6)==4` ensures that the function works correctly in this case.