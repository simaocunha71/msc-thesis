```
    l.sort()
    n = len(l)
    if n % 2 == 0:
        return (l[n//2 - 1] + l[n//2]) / 2
    else:
        return l[n//2]
```


The median of a list of numbers is the middle value in the sorted list. If the list has an even number of elements, the median is the average of the two middle values. The code above sorts the list, then checks whether the list has an odd or even number of elements. If it has an odd number of elements, the median is the middle element. If it has an even number of elements, the median is the average of the two middle elements. The code uses integer division (`//`) to get the index of the middle element(s). The `sort()` method is used to sort the list. The `len()` function is used to get the length of the list. The `+` operator is used to add the two middle elements together, and the `/` operator is used to divide the sum by 2. The `return` statement is used to return the median. The unit tests at the top of the code ensure that the function works correctly for different inputs.