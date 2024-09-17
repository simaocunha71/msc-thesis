```
def frequency(lst, num):
    return lst.count(num)
```
This function takes a list and a number as input, and returns the number of occurrences of the number in the list. The `count` method of the list is used to achieve this. 

For example, if the list is [1,2,3] and the number is 4, the function will return 0 because 4 does not occur in the list. This is confirmed by the unit test `assert frequency([1,2,3], 4) == 0`. 

Please note that this function is case-sensitive and will treat 4 and 4.0 as different numbers. If you want to count the number of occurrences of a number regardless of its type (integer or float), you can convert the list to a set of floats before counting the occurrences. Here is how you can do it:

```
def frequency(lst, num):
    return sum(1 for x in map(float, lst) if x == num)
``` 

This function works by converting each element in the list to a float, then using a generator expression to count the number of elements that are equal to the given number. The `sum` function is then used to add up these counts. 

However, this function will still treat 4 and 4.0 as different numbers. If you want to count the number of occurrences of a number regardless of its type (integer or float) and regardless of its precision (e.g., 4.0 and 4.000000 are considered the same number), you can use the following function:

```
def frequency(lst, num):
    return sum(1 for x in map(str, map(float, lst)) if x == str(num))
``` 

This function works by converting each element in the list to a string, then using a generator expression to count the number of elements that are equal to the string representation of the given number. The `sum` function is then used to add up these counts. 

This function will treat 4 and 4.0 as the same number, and it will also treat 4.0 and 4.000000 as the same number. However, it will still treat 4 and 4.0 as different numbers if they are stored in the list as separate elements. If you want to count the number of occurrences of a number regardless of its type (integer or float) and regardless of its precision, and you also want to count the number