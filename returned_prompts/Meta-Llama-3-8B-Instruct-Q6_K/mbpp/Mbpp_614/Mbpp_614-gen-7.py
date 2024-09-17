```
def cummulative_sum(tuples):
    total = 0
    for tup in tuples:
        total += sum(tup)
    return total
```
The unit test `assert cummulative_sum([(1, 3), (5, 6, 7), (2, 6)]) == 30` ensures that the function correctly calculates the cumulative sum of the values in the tuple list. The function iterates over each tuple in the list, sums up the values in each tuple, and adds the sum to a running total. The total sum is then returned. This approach ensures that the cumulative sum is calculated correctly for tuples of any length. 