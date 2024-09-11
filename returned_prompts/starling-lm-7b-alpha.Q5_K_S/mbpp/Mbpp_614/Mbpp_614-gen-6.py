```
def cummulative_sum(tlist):
    # Initialize cummulative sum
    cummul_sum = 0

    # Iterate through the list and add each element to cummul_sum
    for t in tlist:
        for i in t:
            cummul_sum += i

    return cummul_sum
```

In this function, we initialize a variable `cummul_sum` to 0. Then we use a for loop to go through each tuple in the tuple list. For each tuple, we use another for loop to add up all the values in the tuple to the `cummul_sum` variable. Finally, we return the `cummul_sum` variable, which will be the cumulative sum of all the values in the tuple list.

To check if the function is working correctly, we can use the `assert` keyword to ensure that the function returns the expected result. In this case, we assert that `cummulative_sum([(1, 3), (5, 6, 7), (2, 6)])` is equal to 30. If the function is implemented correctly, this assertion will pass and the function will return the correct cumulative sum.

Here's a step-by-step explanation of the function:

1. Initialize `cummul_sum` to 0. This variable will store the cumulative sum of all the values in the tuple list.
2. Use a for loop to iterate through each tuple in the tuple list.
3. For each tuple, use another for loop to add up all the values in the tuple to the `cummul_sum` variable.
4. After iterating through all the tuples, return the `cummul_sum` variable, which will be the cumulative sum of all the values in the tuple list.
5. Use the `assert` keyword to check if the function returns the expected result (30 in this case). If the function is implemented correctly, this assertion will pass.

By following these steps, we can create a function that calculates the cumulative sum of all the values in a given tuple list.

Here's the code for the function and the assertion:

```python
def cummulative_sum(tlist):
   