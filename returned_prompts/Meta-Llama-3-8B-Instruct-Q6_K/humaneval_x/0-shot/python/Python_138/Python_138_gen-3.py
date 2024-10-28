```
def is_equal_to_sum_even(n):
    for a in range(2, n+1, 2):
        for b in range(2, n+1, 2):
            for c in range(2, n+1, 2):
                for d in range(2, n+1, 2):
                    if a + b + c + d == n:
                        return True
    return False
```


Explanation:
The function is_equal_to_sum_even(n) checks whether the given number n can be written as the sum of exactly 4 positive even numbers. It iterates over all possible combinations of 4 positive even numbers and checks if their sum equals the given number n. If it finds such a combination, it returns True. If it does not find any such combination after checking all possible combinations, it returns False. The time complexity of this function is O(n^2) because it uses nested loops to iterate over all possible combinations of 4 positive even numbers. The space complexity is O(1) because it uses a constant amount of space to store the variables.