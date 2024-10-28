```
def largest_divisor(n: int) -> int:
    for i in range(n-1, 0, -1):
        if n % i == 0:
            return i
```


The function largest_divisor(n) takes an integer n as input and returns the largest integer that divides n evenly, smaller than n. It does this by iterating over the numbers from n-1 down to 1 and checking if each number is a divisor of n. When it finds a divisor, it returns that number. For example, if you call largest_divisor(15), it will return 5 because 5 is the largest number that divides 15 evenly, smaller than 15.