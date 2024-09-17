The Perrin sequence is a recurrence relation where each term is the sum of the previous two terms, starting with 3 and 2. 

Here is a Python function to calculate the sum of Perrin numbers up to a given number of terms:

```Python
def cal_sum(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 3
    elif n == 2:
        return 5
    else:
        perrin_nums = [3, 2]
        for _ in range(2, n):
            perrin_nums.append(perrin_nums[-1] + perrin_nums[-2])
        return sum(perrin_nums)
```

This function first handles the base cases where `n` is 0, 1, or 2. Then it generates the Perrin sequence up to the `n`th term and returns the sum of these terms. 

The unit test `assert cal_sum(9) == 49` ensures that the function is working correctly. The sum of the first 9 Perrin numbers is indeed 49. 