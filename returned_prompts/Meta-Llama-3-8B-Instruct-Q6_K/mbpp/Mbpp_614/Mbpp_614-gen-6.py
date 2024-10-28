The problem is asking to create a function that takes a list of tuples as input and returns the cumulative sum of all the values present in those tuples. 

The given unit test `assert cummulative_sum([(1, 3), (5, 6, 7), (2, 6)]) == 30` suggests that the input will be a list of tuples and the function should return the cumulative sum of all the values in those tuples.

Here is a Python solution for the problem:
```
def cummulative_sum(tuples):
    total = 0
    for tup in tuples:
        total += sum(tup)
    return total
```
This function iterates over each tuple in the input list, calculates the sum of the values in the tuple, and adds it to the total cumulative sum. Finally, it returns the total cumulative sum. 