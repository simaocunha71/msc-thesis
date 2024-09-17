```
def frequency(lst, num):
    return lst.count(num)
```
Explanation:
The problem is asking to write a function that takes a list and a number as input, and returns the number of times the number appears in the list.

The unit test `assert frequency([1,2,3], 4) == 0` suggests that the function should return 0 for the input `[1,2,3]` and `4`, because `4` is not present in the list.

The solution uses the built-in `count` method of Python lists, which returns the number of occurrences of a given element in the list. The function takes two arguments, `lst` and `num`, and returns the result of `lst.count(num)`. This will give the correct count of occurrences of `num` in `lst`. If `num` is not present in `lst`, `lst.count(num)` will return 0, which is the expected result. 