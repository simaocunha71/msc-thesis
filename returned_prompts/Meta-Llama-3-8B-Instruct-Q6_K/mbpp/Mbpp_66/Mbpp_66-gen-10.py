```
def pos_count(lst):
    return sum(1 for x in lst if x > 0)
```
The function `pos_count` takes a list `lst` as input and returns the count of positive numbers in the list. It uses a generator expression to iterate over the list and count the numbers that are greater than 0. The `sum` function is used to calculate the total count. 

The unit test `assert pos_count([1,-2,3,-4]) == 2` ensures that the function correctly counts the positive numbers in the list. 

This solution has a time complexity of O(n) where n is the length of the input list, as it needs to iterate over the list once to count the positive numbers. The space complexity is O(1) as it only uses a constant amount of space to store the count. 