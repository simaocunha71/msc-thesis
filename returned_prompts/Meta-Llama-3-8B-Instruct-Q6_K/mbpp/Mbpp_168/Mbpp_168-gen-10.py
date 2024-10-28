```
def frequency(lst, num):
    return lst.count(num)
```
The problem asks to create a function that counts the number of occurrences of a given number in a list. The function should take two parameters: the list and the number to be counted.

The unit test `assert frequency([1,2,3], 4) == 0` suggests that the function should return 0 when the number is not found in the list.

The solution uses the built-in `count` method of Python lists, which returns the number of occurrences of a specified value in the list. The function `frequency` takes two parameters, `lst` and `num`, and returns the result of `lst.count(num)`. This solution is simple and efficient, with a time complexity of O(n), where n is the length of the list. 