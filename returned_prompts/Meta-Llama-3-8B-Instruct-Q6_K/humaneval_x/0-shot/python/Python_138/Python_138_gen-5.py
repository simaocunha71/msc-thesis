```
def is_equal_to_sum_even(n):
    for a in range(2, n+1):
        for b in range(2, n+1):
            for c in range(2, n+1):
                for d in range(2, n+1):
                    if a + b + c + d == n:
                        return True
    return False
```


Explanation:
The problem requires us to check if a given number `n` can be written as the sum of exactly 4 positive even numbers. 

We can achieve this by using four nested loops to iterate over all possible combinations of even numbers from 2 to `n`. 

If we find a combination of four even numbers that sum up to `n`, we return `True`. If we don't find any such combination after checking all possible combinations, we return `False`.

The time complexity of this solution is O(n^4) because we have four nested loops each of which runs up to `n`. The space complexity is O(1) because we are using a constant amount of space to store the variables and loops. 





Please let me know if you have any further questions.