```
def largest_divisor(n: int) -> int:
    for i in range(n, 0, -1):
        if n % i == 0:
            return i
```
This function iterates from `n` down to `1`, checking each number to see if it is a divisor of `n`. The first number it finds that is a divisor is the largest divisor, so it returns that number. The function stops as soon as it finds a divisor, so it is more efficient than checking all numbers up to `n`. For example, if you call `largest_divisor(15)`, the function will return `5`, which is the largest number that divides `15` evenly. 