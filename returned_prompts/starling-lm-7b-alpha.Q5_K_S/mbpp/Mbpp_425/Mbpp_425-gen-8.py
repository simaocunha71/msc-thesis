```
def count_element_in_list(input_list, element):
    count = 0
    for sublist in input_list:
        if element in sublist:
            count += 1
    return count
```

Explanation:
The function `count_element_in_list` takes two parameters, `input_list` and `element`. It initializes a counter variable `count` to 0. Then, it iterates through each `sublist` in the `input_list`. For each `sublist`, it checks if the `element` is present. If it is, it increments the `count` by 1. Finally, it returns the total count of occurrences of the `element` in the `input_list`.

The given assertion `assert count_element_in_list([[1, 3], [5, 7], [1, 11], [1, 15, 7]],1)==3` checks if the function `count_element_in_list` correctly counts the number of occurrences of the element 1 in the given list. It expects the function to return 3, as there are three sublists containing the element 1.

To use the function, you can call it with the desired input list and element as arguments. For example, to count the occurrences of the element 5 in the list `[[1, 3], [5, 7], [1, 11], [1, 15, 7]]`, you can use `count_element_in_list([[1, 3], [5, 7], [1, 11], [1, 15, 7]], 5)`. This will return the count of occurrences, which in this case is 1.

Overall, the provided solution is a simple and efficient way to count the number of sublists containing a particular element in a given list.

```python
def count_element_in_list(input_list, element):
    count = 0
    for sublist in input_list:
        if element in sublist:
            count += 1
    return count

assert count_element_in_list([[1, 3], [5, 7