```
def sum(n1, n2):
    sum_divisors = 0
    for i in range(1, min(n1, n2) + 1):
        if n1 % i == 0 and n2 % i == 0:
            sum_divisors += i
    return sum_divisors
```


The problem is asking you to write a function that finds the sum of the common divisors of two given numbers. 

The function should iterate over the range from 1 to the smaller of the two numbers (inclusive), and for each number in the range, it should check if it is a divisor of both numbers. If it is, it should add it to the sum of divisors. Finally, it should return the sum of divisors.

The unit test `assert sum(10,15) == 6` helps to clarify the problem by showing that the function should return 6 for the inputs 10 and 15, which is the sum of their common divisors (1, 2, and 5). 

Here's the solution in Python:
```
def sum(n1, n2):
    sum_divisors = 0
    for i in range(1, min(n1, n2) + 1):
        if n1 % i == 0 and n2 % i == 0:
            sum_divisors += i
    return sum_divisors
```


This function works by iterating over the range from 1 to the smaller of the two numbers, and for each number in the range, it checks if it is a divisor of both numbers. If it is, it adds it to the sum of divisors. Finally, it returns the sum of divisors. The unit test `assert sum(10,15) == 6` helps to clarify the problem by showing that the function should return 6 for the inputs 10 and 15, which is the sum of their common divisors (1, 2, and 5).