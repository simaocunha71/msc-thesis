```
def all_unique(lst):
    return len(lst) == len(set(lst))
```

This function works by comparing the length of the input list with the length of a set created from the list. In Python, a set is an unordered collection of unique elements. Therefore, if the lengths are equal, it means that all elements in the list are unique. If the lengths are not equal, it means that there are duplicate elements in the list. The function returns True if the lengths are equal, and False otherwise. This solution passes the given unit test. 





```
assert all_unique([1,2,3]) == True
``` 





```
assert all_unique([1,2,3,3]) == False
``` 





```
assert all_unique([1,2,3,4,5]) == True
``` 





```
assert all_unique([1,2,2,3]) == False
``` 





```
assert all_unique([]) == True
``` 





```
assert all_unique([1]) == True
``` 





```
assert all_unique([1,1]) == False
``` 





```
assert all_unique([1,1,1]) == False
``` 





```
assert all_unique([1,2,3,4,5,6,7,8,9,10]) == True
``` 





```
assert all_unique([1,2,3,4,5,6,7,8,9,10,10]) == False
``` 





```
assert all_unique([1,1,2,3]) == False
``` 





```
assert all_unique([1,2,3,4,5,6,7,8,9,10,11]) == True
``` 





```
assert all_unique([1,2,3,4,5,6,7,8,9,10,11,11]) == False
``` 





```
assert all_unique([1,2,3,4,5,6,7,8,9,10,11,12]) == True
``` 





```
assert all_unique([1,2,3,4,5,6,7,8,9,10,11,12,13]) == True
``` 





```
assert all_unique([1,2,3,4,5,6,7,8,9,10,