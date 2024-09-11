"""
def search(arr):
    n = len(arr)
    if n == 0:
        return "Array is empty"
    if n == 1:
        return arr[0]
    if n == 2:
        if arr[0] == arr[1]:
            return "Array contains only one element"
        else:
            return arr[0]
    for i in range(n-2):
        if arr[i+1] != arr[i] and arr[i+2] != arr[i+1]:
            return arr[i+1]
    if arr[n-2] != arr[n-1]:
        return arr[n-1]


assert search([1,1,2,2,3]) == 3
print(search([1,1,2,2,3]))
"""

def search(arr):
    if len(arr) == 0:
        return "Array is empty"
    if len(arr) == 1:
        return arr[0]
    if len(arr) == 2:
        if arr[0] == arr[1]:
            return "Array contains only one element"
        else:
            return arr[0]
    for i in range(len(arr)-2):
        if arr[i+1] != arr[i] and arr[i+2] != arr[i+1]:
            return arr[i+1]
    if arr[-2] != arr[-1]:
        return arr[-1]


print(search([1,1,2,2,3]))

```
    
In this code, the function `search` takes an array `arr` as an argument and returns the element that appears only once in the array. 

The function first checks if the array is empty or contains only one element. If either of these conditions is true, the function returns the appropriate message or the single element in the array, respectively. 

Next, the function checks if the array contains two elements. If the first element is not equal to the second element, it returns the first element. 

Then, the function iterates through the array, checking if the current element is not equal to the next element and if the next element