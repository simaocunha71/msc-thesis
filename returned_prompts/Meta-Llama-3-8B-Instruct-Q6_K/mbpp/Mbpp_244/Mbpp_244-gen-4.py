```
def next_Perfect_Square(n):
    i = 1
    while True:
        if i ** 2 > n:
            return i ** 2
        i += 1
```


In this problem, we need to find the next perfect square greater than a given number. The problem can be solved by iterating through perfect squares from 1 and checking if the next perfect square is greater than the given number. The function next_Perfect_Square takes an integer n as input and returns the next perfect square greater than n.

The unit test `assert next_Perfect_Square(35) == 36` helps us understand that the function should return the next perfect square greater than the given number. For example, if the input is 35, the function should return 36 because 36 is the next perfect square greater than 35.

The function `next_Perfect_Square` uses a while loop to iterate through perfect squares. It starts from 1 and increments by 1 in each iteration. Inside the loop, it checks if the current perfect square is greater than the given number. If it is, the function returns the current perfect square. If not, it continues to the next iteration. This process continues until the function finds the next perfect square greater than the given number.