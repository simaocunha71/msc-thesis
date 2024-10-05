```
def median(l: list):
    l.sort()
    n = len(l)
    if n % 2 == 0:
        mid1 = l[n//2 - 1]
        mid2 = l[n//2]
        return (mid1 + mid2) / 2
    else:
        return l[n//2]
```


This function sorts the list and then checks if the length of the list is even or odd. If it's even, it calculates the median by taking the average of the two middle elements. If it's odd, it simply returns the middle element. The reason for this is that when the list has an even number of elements, the median is the average of the two middle elements, and when the list has an odd number of elements, the median is the middle element itself. The function also handles the case where the list is empty, in which case it raises an exception. However, in the problem statement, it is not specified what should happen in this case, so the function does not handle it. The function also does not handle the case where the list contains non-numeric elements, so it will raise an exception if this is the case. Again, this is not specified in the problem statement, so the function does not handle it. 

The function also does not handle the case where the list is not a list, so it will raise an exception if this is the case. Again, this is not specified in the problem statement, so the function does not handle it. 

The function uses the built-in list method sort() to sort the list. This method sorts the list in-place, meaning it modifies the original list. It does not return a new list. This is why the function sorts the list before calculating the median. 

The function uses the built-in list method len() to get the length of the list. This method returns the number of elements in the list. 

The function uses the built-in list method // to perform integer division. This method returns the integer part of the division. It is used to calculate the index of the middle element(s) of the list. 

The function uses the built-in list method [ ] to access elements of the list. This method returns the element at the specified index. It is used to access the middle element(s) of the list. 

The function uses the built-in list method + to concatenate lists. This method returns a new list that is the concatenation of the two lists. It is not used