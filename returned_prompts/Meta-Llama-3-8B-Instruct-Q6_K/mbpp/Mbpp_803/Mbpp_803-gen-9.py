```
def is_perfect_square(n):
    if n < 0:
        return False
    if n == 0:
        return True
    i = 1
    while i * i <= n:
        if i * i == n:
            return True
        i += 1
    return False
```    
In this function, we start from 1 and keep increasing the value of i until i * i is greater than n. If i * i equals n at any point, we return True, indicating that n is a perfect square. If we don't find a perfect square by the time i * i is greater than n, we return False. The function also handles the edge cases where n is negative (in which case we return False) or n is 0 (in which case we return True). The unit test `assert not is_perfect_square(10)` ensures that the function correctly identifies 10 as not being a perfect square. 