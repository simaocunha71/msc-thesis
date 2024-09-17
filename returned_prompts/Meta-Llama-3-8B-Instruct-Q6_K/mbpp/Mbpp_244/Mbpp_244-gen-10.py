```
def next_Perfect_Square(n):
    i = n
    while True:
        sq = i ** 0.5
        if sq == int(sq):
            return i
        i += 1
```
This function starts from the given number and keeps incrementing until it finds the next perfect square. It checks if the square root of the number is an integer. If it is, that means the number is a perfect square, so it returns that number. Otherwise, it increments the number and repeats the process.

The unit test `assert next_Perfect_Square(35) == 36` ensures that the function returns the correct result for the given input. In this case, the next perfect square greater than 35 is indeed 36.