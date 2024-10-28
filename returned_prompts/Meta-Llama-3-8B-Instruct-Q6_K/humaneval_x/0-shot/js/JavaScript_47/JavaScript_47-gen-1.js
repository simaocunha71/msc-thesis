Here is the Python solution for the problem:

```Python
def median(l):
    sorted_l = sorted(l)
    length = len(sorted_l)
    if length % 2 == 0:
        mid1 = length // 2 - 1
        mid2 = length // 2
        return (sorted_l[mid1] + sorted_l[mid2]) / 2
    else:
        return sorted_l[length // 2]
```


The median of a list of numbers is the middle value when the list is sorted. If the list has an even number of elements, the median is the average of the two middle values. If the list has an odd number of elements, the median is the middle value. The median is a good measure of the "middle" value of a list, but it is sensitive to outliers (values that are much larger or smaller than the rest of the values). 

This function takes a list of numbers as input, sorts the list, and then calculates the median. If the list has an even number of elements, it calculates the average of the two middle values; if the list has an odd number of elements, it returns the middle value. The function returns the median as a floating-point number. 

This function assumes that the input list is not empty. If the list is empty, the function will raise an exception when it tries to calculate the length of the list. If you want to handle the case where the list is empty, you could add a check at the beginning of the function and return a special value (such as None or a string) to indicate that the list is empty. 

Here is how you can use this function:

```Python
print(median([3, 1, 2, 4, 5]))  # Output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Output: 8.0
```


Please note that the Python code provided is not the same as the original problem description which is written in JavaScript. However, the solution is similar and can be easily translated to JavaScript.