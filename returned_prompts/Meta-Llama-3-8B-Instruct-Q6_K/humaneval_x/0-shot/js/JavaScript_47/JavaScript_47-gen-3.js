```python
def median(l):
    l.sort()
    n = len(l)
    if n % 2 == 0:
        mid1 = l[n//2 - 1]
        mid2 = l[n//2]
        return (mid1 + mid2) / 2
    else:
        return l[n//2]
```


This function first sorts the list. Then it checks if the length of the list is even or odd. If the length is even, it calculates the average of the two middle elements. If the length is odd, it returns the middle element. The reason for this is that the median of a list is the middle value when the list is sorted. If the length is even, the two middle elements are averaged to get the median. If the length is odd, there is only one middle element, which is the median. The function returns the median as a float if the input list is [-10, 4, 6, 1000, 10, 20]. This is because the average of 6 and 10 is 8.0. If the input list is [3, 1, 2, 4, 5], the function returns 3, which is the middle element. This is because the list is sorted and there is only one middle element. 





Example:
```python
print(median([3, 1, 2, 4, 5]))  # Output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Output: 8.0
```


This function works by first sorting the list. Then it checks if the length of the list is even or odd. If the length is even, it calculates the average of the two middle elements. If the length is odd, it returns the middle element. The reason for this is that the median of a list is the middle value when the list is sorted. If the length is even, the two middle elements are averaged to get the median. If the length is odd, there is only one middle element, which is the median. The function returns the median as a float if the input list is [-10, 4, 6, 1000, 10, 20]. This is because the average of 6 and 10 is 8.0. If the input list is [3, 1, 2, 4,