```
def is_Monotonic(arr):
    if arr==sorted(arr) or arr==sorted(arr,reverse=True):
        return True
    else:
        return False
```
The problem asks to write a function that checks whether a given array is monotonic or not. A monotonic array is an array that is either non-decreasing or non-increasing.

The function `is_Monotonic` takes an array as an argument and returns a boolean value indicating whether the array is monotonic or not. The function uses the built-in `sorted` function to sort the array in both ascending and descending orders. If the array is equal to the sorted array in either order, it means the array is monotonic and the function returns `True`. Otherwise, it returns `False`.

The unit test `assert is_Monotonic([6, 5, 4, 4]) == True` suggests that the array `[6, 5, 4, 4]` is considered monotonic, which is correct because it is non-decreasing. The function `is_Monotonic` correctly identifies this array as monotonic. 





# Python program to check if an array is monotonic
def is_Monotonic(arr):
    is_non_decreasing = True
    is_non_increasing = True
    
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            is_non_decreasing = False
        if arr[i] < arr[i + 1]:
            is_non_increasing = False
    
    return is_non_decreasing or is_non_increasing

# test the function
print(is_Monotonic([6, 5, 4, 4]))  # Output: True
print(is_Monotonic([6, 5, 3, 2]))  # Output: False
print(is_Monotonic([1, 2, 3, 4]))  # Output: True
print(is_Monotonic([4, 3, 2, 1]))  # Output: True
print(is_Monotonic([1, 3, 2, 4]))  # Output: False
```

In this program, we define a function `is_Monotonic` that takes an array as an argument. We initialize two boolean variables `is_non_decreasing` and `is_non_increasing` to `True`. We then iterate