```
def frequency(lst, num):
    return lst.count(num)
```
In this problem, we are asked to write a function that counts the number of occurrences of a given number in a list. The function should take two parameters: the list and the number. 

The unit test `assert frequency([1,2,3], 4) == 0` suggests that if the number is not found in the list, the function should return 0. This can be achieved by using the built-in `count` method of the list, which returns the number of occurrences of the given number in the list.

Here is the solution:
```
def frequency(lst, num):
    return lst.count(num)
```  