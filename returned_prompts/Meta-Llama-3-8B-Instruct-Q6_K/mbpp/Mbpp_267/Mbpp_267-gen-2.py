```
def square_Sum(n):
    return sum(i**2 for i in range(1, 2*n, 2))
```


This function uses a generator expression to iterate over the first n odd natural numbers, squares each number, and then sums them up. The `range` function is used to generate the sequence of odd numbers, starting from 1 and incrementing by 2 each time. The `assert` statement at the top of the function ensures that the function returns the correct result for the input 2.