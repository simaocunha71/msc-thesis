The problem asks you to create a function that finds the correct position to insert a new value into a sorted list. The function should return the index where the new value should be inserted to maintain the sorted order.

Here's a Python solution for this problem:

```Python
def right_insertion(lst, value):
    for i in range(len(lst)):
        if lst[i] >= value:
            return i
    return len(lst)
```

This function iterates over the list, comparing each value to the input value. When it finds a value that is greater than or equal to the input value, it returns the index of that value. If the input value is greater than all values in the list, it returns the length of the list, indicating that the value should be appended to the end of the list. 

The unit test `assert right_insertion([1,2,4,5],6)==4` ensures that the function works correctly. It checks that the function returns the correct index (4) when inserting the value 6 into the list [1,2,4,5]. 

The function assumes that the input list is already sorted, and it does not modify the list. It only returns the index where the new value should be inserted. If you want to insert the value into the list, you would use the `insert` method of the list, like this: `lst.insert(right_insertion(lst, value), value)`. 