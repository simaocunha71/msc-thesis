```
def count_element_in_list(input_list, element):
    count = 0
    for sublist in input_list:
        if element in sublist:
            count += 1
    return count
```

Explanation:
To solve the problem, we can define a function called `count_element_in_list` that takes two parameters: `input_list`, which is the list of sublists, and `element`, which is the element we want to count.

Inside the function, we initialize a variable `count` to 0. Then, we iterate over each sublist in the `input_list` using a for loop. For each sublist, we check if the `element` is present in the sublist using the `in` operator. If it is, we increment the `count` by 1.

Finally, we return the value of `count`, which represents the number of sublists containing the `element`.

In the provided example, the function is called with the input `[[1, 3], [5, 7], [1, 11], [1, 15, 7]]` and the element `1`. The function will count the number of sublists that contain the element `1` and return the result, which is 3.

To verify the correctness of the function, an assertion is used to check if the returned value of the function is equal to the expected result. In this case, the assertion `assert count_element_in_list([[1, 3], [5, 7], [1, 11], [1, 15, 7]],1)==3` is used to ensure that the function returns the correct value of 3.

Overall, the provided solution is a simple and efficient way to count the number of sublists containing a particular element in a given list of sublists.

```python
def count_element_in_list(input_list, element):
    count = 0
    for sublist in input_list:
        if element in sublist:
            count += 1
    return count
```

This implementation uses a nested loop to iterate over each sublist in the input list. For each sublist, it checks if the element