```
def can_arrange(arr):
    for i in range(len(arr) - 1):
        if arr[i + 1] <= arr[i]:
            return i
    return -1
```


The function iterates through the array and checks if the current element is greater than or equal to the next element. If it finds such an element, it returns the index of that element. If no such element is found, it returns -1. The function uses the fact that the array does not contain duplicate values to ensure that the loop will terminate and return -1 if no such element is found. 

For example, in the array [1,2,4,3,5], the function will return 3 because the element at index 3 (3) is not greater than or equal to the element immediately preceding it (4). In the array [1,2,3], the function will return -1 because no element in the array is not greater than or equal to the element immediately preceding it. 

This function has a time complexity of O(n), where n is the length of the array, because it iterates through the array once. It has a space complexity of O(1), because it uses a constant amount of space to store the index and the current element. 