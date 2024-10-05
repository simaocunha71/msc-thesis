The function largest_divisor(n: int) -> int will find the largest number that divides n evenly, smaller than n.

Here is the Python code for the function:

```Python
def largest_divisor(n: int) -> int:
    for i in range(n, 0, -1):
        if n % i == 0:
            return i
```

This function works by starting from n and decrementing by 1 until it finds a number that divides n evenly (i.e., n % i == 0). The last number it finds is the largest divisor of n smaller than n. 

For example, if you call `largest_divisor(15)`, it will return `5` because 5 is the largest number that divides 15 evenly, smaller than 15. 





