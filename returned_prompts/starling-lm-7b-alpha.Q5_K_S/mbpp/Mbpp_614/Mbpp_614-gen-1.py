```
def cummulative_sum(tuple_list):
    total = 0
    for tup in tuple_list:
        total += sum(tup)
    return total
```

Explanation:
In this case, the function `cummulative_sum` takes in a list of tuples as an argument and returns the cumulative sum of all the values in the tuples. 

To achieve this, we initialize a variable `total` to 0, which will keep track of the cumulative sum. Then, we iterate through each tuple in the `tuple_list`. For each tuple, we use the `sum` function to calculate the sum of all the values in the tuple and add this sum to the `total` variable. 

Finally, we return the `total` variable, which represents the cumulative sum of all the values in the given tuple list.

In the provided example, `cummulative_sum([(1, 3), (5, 6, 7), (2, 6)])` will return 30, as the cumulative sum of all the values in the tuples is 1 + 3 + 5 + 6 + 7 + 2 + 6 = 30.

This solution can be easily extended to handle any number of tuples and values, as long as the input is in the correct format.

To verify the correctness of the function, an assertion is used to check if the function returns the expected result for the given example. If the assertion fails, an error will be raised, indicating that the function is not working correctly.

Overall, the provided code is a simple and efficient solution to calculate the cumulative sum of all the values in a given tuple list.

```python
def cummulative_sum(tuple_list):
    total = 0
    for tup in tuple_list:
        total += sum(tup)
    return total

# To verify the correctness of the function
assert cummulative_sum([(1, 3), (5, 6, 7), (2, 6)]) == 30
```

The `cummulative_sum` function can be easily tested by using the `assert` keyword to check if the function returns the