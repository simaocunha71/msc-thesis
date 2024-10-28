```
def larg_nnum(lst, n):
    return sorted(lst, reverse=True)[:n]
```
This function sorts the list in descending order and then returns the first n items. 

The unit test `assert set(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],2))==set([100,90])` ensures that the function returns the n largest items from the list. 

However, this function does not remove duplicates. If the list contains duplicate items and the function is supposed to return unique items, then this function would need to be modified to remove duplicates. 

For example, the unit test `assert set(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],2))==set([100,90])` suggests that the function should return unique items, so the function would need to be modified to return the n most frequent unique items. 

Here is an updated version of the function that returns the n most frequent unique items:
```
from collections import Counter
def larg_nnum(lst, n):
    counter = Counter(lst)
    return [item[0] for item in counter.most_common(n)]
```
This function uses the Counter class from the collections module to count the frequency of each item in the list, and then returns the n most common items. 

The unit test `assert set(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],2))==set([100,90])` ensures that the function returns the n most frequent unique items. 

Note that this function returns the n most frequent items, not the n largest items. If the function is supposed to return the n largest items, then the original function would need to be modified to remove duplicates. 

Here is an updated version of the function that removes duplicates and returns the n largest items:
```
def larg_nnum(lst, n):
    lst = list(set(lst))
    return sorted(lst, reverse=True)[:n]
```
This function removes duplicates by converting the list to a set and then back to a list, and then returns the n largest items. 

The unit test `assert set(larg_nnum([10, 20, 50