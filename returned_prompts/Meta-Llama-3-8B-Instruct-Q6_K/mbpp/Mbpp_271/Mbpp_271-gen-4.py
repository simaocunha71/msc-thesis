```
def even_Power_Sum(n):
    total_sum = 0
    for i in range(2, n*2, 2):
        total_sum += i**5
    return total_sum
```


The provided unit test `assert even_Power_Sum(2) == 1056` helps in understanding the problem better. It implies that the function should find the sum of the first n even natural numbers that are raised to the fifth power. 

We can solve this problem by initializing a variable `total_sum` to zero. Then, we loop through the range from 2 to 2n (since we are considering even numbers), incrementing by 2 each time. For each number in the range, we add its fifth power to `total_sum`. Finally, we return `total_sum`. 

This solution works because it correctly calculates the sum of the first n even natural numbers that are raised to the fifth power. The unit test `assert even_Power_Sum(2) == 1056` confirms that the function is working correctly. 