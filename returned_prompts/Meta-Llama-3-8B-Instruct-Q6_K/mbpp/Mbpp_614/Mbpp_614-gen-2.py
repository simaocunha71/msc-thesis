```
def cummulative_sum(tuples):
    total = 0
    for t in tuples:
        total += sum(t)
    return total
```


The given problem is asking to find the cumulative sum of all the values that are present in the given tuple list. The input is a list of tuples, and the function should return the cumulative sum of all the values in the tuples. For example, if the input is `[(1, 3), (5, 6, 7), (2, 6)]`, the function should return `30`, which is the sum of `1 + 3 + 5 + 6 + 7 + 2 + 6`.

The unit test `assert cummulative_sum([(1, 3), (5, 6, 7), (2, 6)]) == 30` helps to clarify the problem by providing an example of the expected output.

Here is the solution to the problem:
```
def cummulative_sum(tuples):
    total = 0
    for t in tuples:
        total += sum(t)
    return total
```
This function uses a for loop to iterate over each tuple in the list. For each tuple, it uses the built-in `sum` function to add up all the values in the tuple and adds the result to the `total` variable. Finally, it returns the `total` variable, which is the cumulative sum of all the values in the tuples.