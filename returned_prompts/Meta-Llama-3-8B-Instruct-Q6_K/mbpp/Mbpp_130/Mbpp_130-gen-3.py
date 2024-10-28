```
def max_occurrences(lst):
    from collections import Counter
    counter = Counter(lst)
    return max(counter, key=counter.get)
```
This function uses the Counter class from the collections module to count the frequency of each item in the list. It then returns the item with the maximum frequency using the max function with the key argument set to the get method of the Counter object. This is a one-liner solution that passes the given unit test. 

The unit test `assert max_occurrences([2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,2]) == 2` ensures that the function correctly returns the item with the maximum frequency, which is 2 in this case. 

This solution assumes that the input list is non-empty. If the input list is empty, the function will raise a KeyError. If the list contains multiple items with the same maximum frequency, the function will return one of them. If you want to return all items with the maximum frequency, you would need to modify the function accordingly. 