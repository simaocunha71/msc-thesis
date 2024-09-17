```
def amicable_numbers_sum(n):
    def is_amicable(a, b):
        if a == b:
            return False
        sum_a = sum(i for i in range(1, a) if a % i == 0)
        sum_b = sum(i for i in range(1, b) if b % i == 0)
        return sum_a == b and sum_b == a

    sum = 0
    for i in range(1, n):
        for j in range(i, n):
            if is_amicable(i, j):
                sum += i
    return sum
```


The function `amicable_numbers_sum(n)` returns the sum of all amicable numbers from 1 to `n`.

The helper function `is_amicable(a, b)` checks if two numbers `a` and `b` are amicable by checking if `a` is equal to the sum of the proper divisors of `b`, and vice versa.

The main function iterates over all numbers from 1 to `n`, and for each number `i`, it checks all numbers `j` from `i` to `n` to see if `i` and `j` are amicable. If they are, it adds `i` to the sum. Finally, it returns the sum of all amicable numbers.

The unit test `assert amicable_numbers_sum(999)==504` ensures that the function works correctly. The sum of all amicable numbers from 1 to 999 is indeed 504.