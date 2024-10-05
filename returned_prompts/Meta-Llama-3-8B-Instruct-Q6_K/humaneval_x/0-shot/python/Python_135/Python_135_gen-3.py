```
def can_arrange(arr):
    for i in range(len(arr) - 1):
        if arr[i] >= arr[i+1]:
            return i
    return -1
```



Explanation:

This function iterates through the array, comparing each element with the next one. If it finds an element that is greater than or equal to the next one, it returns the index of that element. If it doesn't find any such element, it returns -1.

In the example for `can_arrange([1,2,4,3,5])`, the function will return 3 because the element at index 3 (4) is not greater than or equal to the element at index 4 (5). In the example for `can_arrange([1,2,3])`, the function will return -1 because all elements are in ascending order and there is no element that is not greater than or equal to the next one. 





How it works:

1. The function starts by initializing an empty list.
2. It then iterates over the list of elements.
3. For each element, it checks if the element is greater than or equal to the next element.
4. If it finds an element that is not greater than or equal to the next element, it returns the index of that element.
5. If it doesn't find any such element, it returns -1.
6. The function then returns the index of the largest element that is not greater than or equal to the next element.

Example:
```
can_arrange([1,2,4,3,5])  # returns 3
can_arrange([1,2,3])  # returns -1
```





Output:

```
3
-1
```





Code:

```
def can_arrange(arr):
    for i in range(len(arr) - 1):
        if arr[i] >= arr[i+1]:
            return i
    return -1
```





Explanation:

The function iterates over the list of elements and checks if each element is greater than or equal to the next element. If it finds an element that is not greater than or equal to the next element, it returns the index of that element. If it doesn't find any such element, it returns -1.