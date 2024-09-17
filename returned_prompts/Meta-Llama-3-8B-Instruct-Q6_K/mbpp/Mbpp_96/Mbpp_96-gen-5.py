```
def divisor(n):
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count += 1
    return count
```    
Explanation:
The function `divisor(n)` takes an integer `n` as input and returns the number of its divisors. It iterates over all numbers from 1 to `n` and checks if `n` is divisible by each number. If it is, it increments the count. Finally, it returns the count. The unit test `assert divisor(15) == 4` ensures that the function works correctly, as 15 has 4 divisors: 1, 3, 5, and 15.  The function has a time complexity of O(n) because it checks every number from 1 to `n`. It can be optimized by using a more efficient algorithm, such as checking only numbers up to the square root of `n`. However, for small values of `n`, this function is sufficient and easy to understand. 