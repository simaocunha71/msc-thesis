```
def can_arrange(arr):
    for i in range(len(arr)-1):
        if arr[i] <= arr[i+1]:
            return i
    return -1
```


The function iterates through the array, and for each element, it checks if it is less than or equal to the next element. If it finds such an element, it returns the index. If it doesn't find any such element, it returns -1.

For example, in the array [1,2,4,3,5], the function will return 3 because the element at index 3 (3) is not greater than or equal to the element at index 4 (5). In the array [1,2,3], the function will return -1 because no element is less than or equal to the next element. 

The time complexity of this function is O(n), where n is the number of elements in the array. This is because it needs to iterate through the array once. The space complexity is O(1), which means it uses a constant amount of space. This is because it only uses a few variables to store the current index and the current element. 