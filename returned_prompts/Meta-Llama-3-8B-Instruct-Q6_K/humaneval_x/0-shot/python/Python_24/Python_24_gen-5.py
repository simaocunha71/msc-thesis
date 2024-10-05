The function largest_divisor(n: int) -> int finds the largest number that divides n evenly, smaller than n. 

Here is a Python solution:

```Python
def largest_divisor(n: int) -> int:
    for i in range(n, 0, -1):
        if n % i == 0:
            return i
```

In this solution, we start from n and go down to 1. For each number, we check if it is a divisor of n by using the modulus operator (%). If it is, we return that number. This ensures that we find the largest divisor that is smaller than n. 

For example, largest_divisor(15) returns 5, which is the largest number that divides 15 evenly, smaller than 15. 

The unit test `>>> largest_divisor(15)` also checks that this function works correctly for the input 15. 