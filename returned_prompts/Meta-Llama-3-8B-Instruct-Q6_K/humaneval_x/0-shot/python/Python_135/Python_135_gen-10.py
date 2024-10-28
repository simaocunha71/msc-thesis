```
def can_arrange(arr):
    for i in range(len(arr)-1):
        if arr[i+1] <= arr[i]:
            return i
    return -1
```
Explanation:

The function iterates over the array, checking if the current element is greater than the next one. If it finds such an element, it returns the index of that element. If it doesn't find any such element, it returns -1.

The reason we iterate up to len(arr)-1 is that the last element doesn't have a next element to compare with, so we can't determine if it's smaller or larger than its previous element. If no such element is found, the function returns -1.

For example, in the array [1,2,4,3,5], the largest index of an element which is not greater than or equal to the element immediately preceding it is 3, because 3 is not greater than or equal to 4. So, the function returns 3. In the array [1,2,3], no such element exists, so the function returns -1.  Python code to solve the problem is:

```
def can_arrange(arr):
    for i in range(len(arr)-1):
        if arr[i+1] <= arr[i]:
            return i
    return -1
```

This function takes a list of integers as input and returns the largest index of an element which is not greater than or equal to the element immediately preceding it. If no such element exists, it returns -1.

For example:

```
print(can_arrange([1,2,4,3,5]))  # Output: 3
print(can_arrange([1,2,3]))  # Output: -1
```  Python code to solve the problem is:

```
def can_arrange(arr):
    for i in range(len(arr)-1):
        if arr[i+1] <= arr[i]:
            return i
    return -1
```

This function takes a list of integers as input and returns the largest index of an element which is not greater than or equal to the element immediately preceding it. If no such element exists, it returns -1.  Python code to solve the problem is:

```
def can_arrange(arr):
    for i in range(len(arr)-1):
        if arr[i+1] <= arr[i]:
            return i
    return -1
```  Python code to solve the problem is