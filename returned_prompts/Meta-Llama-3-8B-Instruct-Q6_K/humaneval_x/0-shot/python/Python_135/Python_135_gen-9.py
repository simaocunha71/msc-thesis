```
def can_arrange(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i+1]:
            return i
    return -1
```


The function `can_arrange(arr)` iterates over the array, checking if each element is greater than the one preceding it. If it finds an element that is not greater than the one preceding it, it returns the index of that element. If it doesn't find such an element, it returns -1.

In the given examples, `can_arrange([1,2,4,3,5])` returns 3 because the element at index 3 (3) is not greater than the one preceding it (5). `can_arrange([1,2,3])` returns -1 because all elements in the array are greater than or equal to the one preceding it. 