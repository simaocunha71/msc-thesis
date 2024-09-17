```
def odd_num_sum(n):
    return sum(i**4 for i in range(1, 2*n+1, 2))
```


This function uses a generator expression to iterate over the first n odd natural numbers, squares each number, and sums them up. The `range` function is used to generate the sequence of odd numbers, starting from 1 and incrementing by 2 each time. The `**` operator is used to compute the fourth power of each number. The `sum` function is used to compute the sum of the fourth powers.

The unit test `assert odd_num_sum(2) == 82` ensures that the function works correctly for the input n=2. For this input, the function should return the sum of the fourth powers of the first 2 odd natural numbers, which is 1^4 + 3^4 = 1 + 81 = 82. 





```python
def odd_num_sum(n):
    return sum(i**4 for i in range(1, 2*n+1, 2))
```





The unit test `assert odd_num_sum(2) == 82` ensures that the function works correctly for the input n=2. For this input, the function should return the sum of the fourth powers of the first 2 odd natural numbers, which is 1^4 + 3^4 = 1 + 81 = 82.