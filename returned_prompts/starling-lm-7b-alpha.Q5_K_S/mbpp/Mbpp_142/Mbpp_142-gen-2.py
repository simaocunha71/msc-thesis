```
def count_samepair(list1, list2, list3):
    count = 0
    for i in range(len(list1)):
        if list1[i] == list2[i] == list3[i]:
            count += 1
    return count
```

To test the function, you can use the following code:

```python
assert count_samepair([1,2,3,4,5,6,7,8],[2,2,3,1,2,6,7,9],[2,1,3,1,2,6,7,9])==3
```

This function `count_samepair` takes three lists as input and returns the number of items that are identical in the same position in all three lists. It iterates through the indices of the lists using the `range(len(list1))` construct. Inside the loop, it checks if the elements at the current index in all three lists are equal using the comparison `list1[i] == list2[i] == list3[i]`. If they are equal, it increments the `count` variable by one. Finally, it returns the `count` variable, which represents the total number of identical items in the same position of the three given lists.

The provided assert statement is used to test the function and ensure that it returns the expected result. In this case, it asserts that `count_samepair` returns 3 when given the three lists `[1,2,3,4,5,6,7,8]`, `[2,2,3,1,2,6,7,9]`, and `[2,1,3,1,2,6,7,9]`.

You can run the assert statement to verify the correctness of the function implementation.

```python
assert count_samepair([1,2,3,4,5,6,7,8],[2,2,3,1,2,6,7,9],[2,1,3,1,2,6,7,9])==3
```

If the assertion passes, it means that the function correctly counts the number of identical items in the same position of the three given lists, and the result is indeed 