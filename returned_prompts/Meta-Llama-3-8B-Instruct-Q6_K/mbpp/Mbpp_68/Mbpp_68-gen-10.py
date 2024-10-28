```
def is_Monotonic(arr):
    is_increasing = is_decreasing = False
    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            is_increasing = True
        elif arr[i] < arr[i-1]:
            is_decreasing = True
        else:
            continue
    return is_increasing or is_decreasing

assert is_Monotonic([6, 5, 4, 4]) == True
```


The function checks whether the given array is monotonic or not. A monotonic array is either monotonically increasing or monotonically decreasing. The function first initializes two boolean variables, is_increasing and is_decreasing, to False. Then, it iterates over the array from the second element to the last. If it finds an element that is greater than the previous one, it sets is_increasing to True. If it finds an element that is less than the previous one, it sets is_decreasing to True. If it does not find any such elements, it returns False. If it finds at least one increasing or decreasing sequence, it returns True. The unit test ensures that the function works correctly for the array [6, 5, 4, 4]. 





Note: In Python, we can also use built-in functions like sorted() and sorted(arr) to check if the array is monotonic. However, this solution is more intuitive and easier to understand. 

Here is the Python code using built-in functions:

```
def is_Monotonic(arr):
    return arr == sorted(arr) or arr == sorted(arr, reverse=True)

assert is_Monotonic([6, 5, 4, 4]) == True
```

This code checks if the array is either monotonically increasing (sorted(arr)) or monotonically decreasing (sorted(arr, reverse=True)). If the array is either of these, it returns True. Otherwise, it returns False. The unit test ensures that the function works correctly for the array [6, 5, 4, 4].