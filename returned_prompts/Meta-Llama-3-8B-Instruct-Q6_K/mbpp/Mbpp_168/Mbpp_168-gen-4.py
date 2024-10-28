```
def frequency(lst, num):
    return lst.count(num)
```





Note: This problem is asking you to create a function that counts the number of times a specific number appears in a given list. The function should take two parameters: the list and the number to be counted.

The unit test provided, `assert frequency([1,2,3], 4) == 0`, suggests that if the number is not found in the list, the function should return 0. This can be achieved by using the built-in `count` method of Python lists, which returns the number of occurrences of the specified value.

Here's the solution:
```
def frequency(lst, num):
    return lst.count(num)
```
This function takes a list `lst` and a number `num` as input, and returns the number of times `num` appears in `lst`. If `num` is not found in `lst`, the function returns 0.