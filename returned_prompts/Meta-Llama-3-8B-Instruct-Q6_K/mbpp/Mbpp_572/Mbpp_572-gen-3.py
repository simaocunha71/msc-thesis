```
def two_unique_nums(lst):
    return list(set([i for i in lst if lst.count(i) == 1]))
```


This function uses a list comprehension to create a list of numbers that appear only once in the input list. The `set` function is used to remove duplicates, and then the list is converted back to a list. The `lst.count(i) == 1` condition ensures that only numbers that appear only once are included in the result. 

For example, if the input is `[1,2,3,2,3,4,5]`, the function will return `[1, 4, 5]`, which are the numbers that appear only once in the input list. 

This solution has a time complexity of O(n^2) due to the use of the `count` method inside the list comprehension, which has a linear time complexity. If the input list is very large, this function may be slow. A more efficient solution would be to use a dictionary to count the occurrences of each number, which would have a time complexity of O(n). 

Here is an example of how to use a dictionary to count the occurrences of each number:

```
def two_unique_nums(lst):
    counts = {}
    for num in lst:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    return [num for num, count in counts.items() if count == 1]
```

This function has a time complexity of O(n) and is more efficient than the original solution for large input lists. 

Note that the unit test `assert two_unique_nums([1,2,3,2,3,4,5]) == [1, 4, 5]` ensures that the function returns the correct result for the given input. 

The unit test `assert two_unique_nums([1,1,1]) == []` ensures that the function returns an empty list when all numbers appear more than once. 

The unit test `assert two_unique_nums([1,2,3]) == [1, 2, 3]` ensures that the function returns the correct result when all numbers appear only once. 

These unit tests help to ensure that the function works correctly for different input scenarios. 

The function can be further improved by adding error handling to handle invalid input, such as non-integer values or empty lists. 

The function can also be improved by adding a check to