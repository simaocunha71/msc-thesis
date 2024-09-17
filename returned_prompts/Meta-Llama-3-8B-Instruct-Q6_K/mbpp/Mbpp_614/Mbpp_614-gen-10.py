```
def cummulative_sum(tuple_list):
    total = 0
    for t in tuple_list:
        total += sum(t)
    return total
```
The problem is asking to find the cumulative sum of all the values that are present in the given tuple list. The cumulative sum is the sum of all the values in the tuples. 

The function takes a list of tuples as input, iterates over each tuple in the list, sums up the values in the tuple, and adds this sum to the total. Finally, it returns the total cumulative sum.

The unit test `assert cummulative_sum([(1, 3), (5, 6, 7), (2, 6)]) == 30` helps to understand the problem better. It shows that the function should sum all the values in the tuples and return the total sum. 

For example, in the tuple list `[(1, 3), (5, 6, 7), (2, 6)]`, the function should calculate the sum as follows: `1 + 3 = 4`, `5 + 6 + 7 = 18`, `2 + 6 = 8`, and then return the cumulative sum `4 + 18 + 8 = 30`. 