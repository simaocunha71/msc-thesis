```
def sequential_search(arr, element):
    for i in range(len(arr)):
        if arr[i] == element:
            return (True, i)
    return (False, -1)
```
This function uses a for loop to iterate over the array. If the element is found, it returns a tuple with a boolean value of True and the index position of the element. If the element is not found after iterating over the entire array, it returns a tuple with a boolean value of False and an index position of -1. The unit test provided ensures that the function works correctly.