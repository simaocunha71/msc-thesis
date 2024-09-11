```
def count_samepair(list1, list2, list3):
    count = 0
    for i in range(len(list1)):
        if list1[i] == list2[i] == list3[i]:
            count += 1
    return count
```

The function `count_samepair` is defined to take three lists as input and returns the count of items that are identical in the same position of the three given lists.

To achieve this, a `for` loop is used to iterate through the indices of the first list. Inside the loop, an `if` statement is used to check if the items at the same index in all three lists are equal. If they are, the count variable is incremented by 1. Finally, the count is returned as the result.

In the provided assertion, the function is tested with three lists: `[1,2,3,4,5,6,7,8]`, `[2,2,3,1,2,6,7,9]`, and `[2,1,3,1,2,6,7,9]`. The expected result is 3, as there are three pairs of identical items in the same position in all three lists.

To use the function, simply call it with the three lists as arguments, like this:
```python
print(count_samepair([1,2,3,4,5,6,7,8],[2,2,3,1,2,6,7,9],[2,1,3,1,2,6,7,9]))
```
This will output `3`, indicating that there are three pairs of identical items in the same position in all three lists.

Overall, the function `count_samepair` provides a straightforward way to count the number of identical items in the same position of three given lists.

























































































