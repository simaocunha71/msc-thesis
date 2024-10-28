```
def odd_num_sum(n):
    return sum([i**4 for i in range(1, 2*n, 2)])
```


This function uses a list comprehension to generate the first `n` odd natural numbers, squares each number, and then sums the results. The `range(1, 2*n, 2)` generates the first `n` odd natural numbers. 

The unit test `assert odd_num_sum(2) == 82` checks if the function works correctly for the input `n=2`. 

The function returns the sum of the fourth powers of the first `n` odd natural numbers. For example, for `n=2`, the function returns `1**4 + 3**4 = 1 + 81 = 82`. 