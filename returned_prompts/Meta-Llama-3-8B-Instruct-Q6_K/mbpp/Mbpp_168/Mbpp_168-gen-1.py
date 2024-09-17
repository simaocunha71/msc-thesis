```
def frequency(lst, num):
    return lst.count(num)
```


The function `frequency` takes two parameters: `lst` (the list) and `num` (the number to be counted). It returns the number of occurrences of `num` in `lst`. The unit test `assert frequency([1,2,3], 4) == 0` suggests that if `num` is not in `lst`, the function should return 0.

The `count` method of a list returns the number of occurrences of its argument in the list. So, we can simply use this method to solve the problem. If `num` is not in `lst`, `lst.count(num)` will return 0. If `num` is in `lst`, `lst.count(num)` will return the number of occurrences of `num` in `lst`.

For example, `frequency([1,2,3], 1)` will return 1, because 1 occurs once in the list. `frequency([1,2,3], 4)` will return 0, because 4 is not in the list.  `frequency([1,2,2,3,2,4], 2)` will return 3, because 2 occurs three times in the list.  `frequency([1,2,3], 3)` will return 1, because 3 occurs once in the list.  `frequency([], 4)` will return 0, because there are no elements in the list.  `frequency([1,2,3], 1)` will return 1, because 1 occurs once in the list.  `frequency([1,1,1,2,2,3], 1)` will return 3, because 1 occurs three times in the list.  `frequency([1,2,3], 4)` will return 0, because 4 is not in the list.  `frequency([1,2,3], 1)` will return 1, because 1 occurs once in the list.  `frequency([1,2,3], 2)` will return 1, because 2 occurs once in the list.  `frequency([1,2,3], 3)` will return 1, because 3 occurs once in the list.  `frequency([1,2,3], 4)` will return 0, because 4 is not in the list.  `