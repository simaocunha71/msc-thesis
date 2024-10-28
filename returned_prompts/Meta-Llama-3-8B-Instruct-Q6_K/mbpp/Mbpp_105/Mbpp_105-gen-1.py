```
def count(lst):
    return lst.count(True)
```


Explanation:
The problem is asking to create a function that counts the number of true boolean values in a given list. 

The unit test provided suggests that the function should return 2 when given the list [True, False, True]. This means the function should count the number of True values in the list.

The solution uses the built-in count method of Python lists, which returns the number of occurrences of the given element in the list. In this case, the element is True. The function simply returns the result of this method call.

This solution passes the given unit test. However, it's worth noting that this solution does not handle the case where the list contains other types of values, not just booleans. If the list contains other types of values, the count method will return 0, because it only counts the occurrences of the exact object True, not boolean values in general. If you want to count boolean values in general, you would need a different solution. 