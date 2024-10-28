```
def count_Occurrence(t, lst):
    from collections import Counter
    t = tuple(t)
    lst = tuple(lst)
    return sum(Counter(t)[i] for i in lst)
```
This function uses the Counter class from the collections module to count the occurrences of each element in the tuple. It then sums up the counts for the elements in the list.

The unit test `assert count_Occurrence(('a', 'a', 'c', 'b', 'd'),['a', 'b'] ) == 3` helps to clarify that the function should return the total count of the elements in the list, not a dictionary of the counts. 

The function can also be written without using the Counter class:
```
def count_Occurrence(t, lst):
    from collections import Counter
    t = tuple(t)
    lst = tuple(lst)
    return sum(t.count(i) for i in lst)
```
This function uses the count method of the tuple to count the occurrences of each element in the tuple, and then sums up the counts for the elements in the list. 

However, this function is less efficient than the previous one, especially for large inputs, because it has to iterate over the tuple for each element in the list. The previous function is more efficient because it uses the Counter class to count the occurrences of all elements in the tuple in one iteration. 