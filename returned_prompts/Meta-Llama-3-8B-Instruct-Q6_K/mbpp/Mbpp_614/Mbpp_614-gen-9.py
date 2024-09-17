```
def cummulative_sum(tuples_list):
    result = 0
    for t in tuples_list:
        result += sum(t)
    return result
```


Here is the explanation of the code:

1. We initialize a variable `result` to 0, which will store the cumulative sum of all the values in the tuple list.
2. We iterate over each tuple in the tuple list.
3. For each tuple, we calculate the sum of all the values in the tuple using the `sum()` function.
4. We add this sum to the `result` variable.
5. Finally, we return the `result` variable, which now contains the cumulative sum of all the values in the tuple list. 
6. We test the function with the given unit test `assert cummulative_sum([(1, 3), (5, 6, 7), (2, 6)]) == 30` and it passes. 

This function will work for any tuple list, not just the one given in the unit test. It will correctly calculate the cumulative sum of all the values in the tuple list. 







