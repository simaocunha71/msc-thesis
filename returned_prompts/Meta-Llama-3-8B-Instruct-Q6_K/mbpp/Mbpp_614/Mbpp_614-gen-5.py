```
def cummulative_sum(tuple_list):
    total = 0
    for t in tuple_list:
        total += sum(t)
    return total
```


The provided unit test `assert cummulative_sum([(1, 3), (5, 6, 7), (2, 6)]) == 30` helps in understanding the problem better. It suggests that we need to find the cumulative sum of all the values that are present in the given tuple list. 

The function `cummulative_sum` iterates over each tuple in the list, calculates the sum of its elements, and adds it to the total sum. Finally, it returns the total sum. 

In the given unit test, the function `cummulative_sum` should return `30` when given the tuple list `[(1, 3), (5, 6, 7), (2, 6)]`. This is because the sum of the elements in this tuple list is `1 + 3 + 5 + 6 + 7 + 2 + 6 = 30`. 