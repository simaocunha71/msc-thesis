```
def is_equal_to_sum_even(n):
    for i in range(2, n+1, 2):
        for j in range(2, n+1, 2):
            for k in range(2, n+1, 2):
                for l in range(2, n+1, 2):
                    if i + j + k + l == n:
                        return True
    return False
```


This function uses nested loops to check all possible combinations of 4 positive even numbers. It starts from 2 and goes up to n with a step of 2 (since even numbers are in the form 2k, where k is an integer). For each combination, it checks if the sum of the numbers is equal to the given number n. If it finds a combination that satisfies this condition, it returns True. If it doesn't find any such combination after checking all possibilities, it returns False.