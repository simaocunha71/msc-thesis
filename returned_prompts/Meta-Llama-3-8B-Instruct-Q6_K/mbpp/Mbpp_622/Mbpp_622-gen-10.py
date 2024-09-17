```
def get_median(list1, list2, size):
    combined = sorted(list1 + list2)
    return combined[size//2] if size % 2 else (combined[size//2 - 1] + combined[size//2]) / 2
```


The function takes two sorted lists of the same size and returns the median of the combined list. The combined list is sorted first. The median is calculated as the middle value if the list size is odd, and as the average of the two middle values if the list size is even. The unit test `assert get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 5) == 16.0` helps to clarify the problem and ensure the function works correctly. 

The function uses integer division (`//`) to calculate the index of the middle value. If the list size is even, it calculates the average of the two middle values by adding them and dividing by 2. The function returns the median as a float if the list size is even. 

The time complexity of the function is O(n log n) due to the sorting operation, where n is the size of the input lists. The space complexity is O(n) for storing the combined list. 
```python
def get_median(list1, list2, size):
    combined = sorted(list1 + list2)
    return combined[size//2] if size % 2 else (combined[size//2 - 1] + combined[size//2]) / 2
``` 
Please note that this solution assumes that the input lists are of the same size. If the lists can be of different sizes, the function should be modified to handle this case. 

Also, the function does not handle the case where the input lists are not sorted. In a real-world scenario, you would want to add error checking to handle these cases. 
```python
def get_median(list1, list2, size):
    if len(list1) != len(list2):
        raise ValueError("Input lists must be of the same size")
    if not all(list1[i] <= list1[i+1] for i in range(len(list1)-1)) or not all(list2[i] <= list2[i+1] for i in range(len(list2)-1)):
        raise ValueError("Input lists must be sorted")
    combined = sorted(list1 + list2)
    return