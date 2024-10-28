```
def is_equal_to_sum_even(n):
    for i in range(2, n, 2):
        for j in range(i, n, 2):
            for k in range(j, n, 2):
                for l in range(k, n, 2):
                    if i + j + k + l == n:
                        return True
    return False
```


Note: This function checks all possible combinations of 4 positive even numbers to see if they sum up to the given number. If it finds a combination that sums up to the given number, it returns True; otherwise, it returns False. 

This function may not be efficient for large inputs because it checks all possible combinations of 4 positive even numbers. It would be more efficient to use a more advanced algorithm or data structure, such as dynamic programming or a set, to find the combinations that sum up to the given number. 

Also, please note that this function assumes that the input number n is a positive integer. If the input number can be negative or zero, you may need to add additional checks or handling. 