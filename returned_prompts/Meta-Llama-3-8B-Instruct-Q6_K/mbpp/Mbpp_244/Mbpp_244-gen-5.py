```
def next_Perfect_Square(n):
    i = int(n ** 0.5) + 1
    while True:
        square = i * i
        if square > n:
            return square
        i += 1
```


Explanation:
The problem asks to find the next perfect square greater than a given number. A perfect square is a number that can be expressed as the square of an integer.

The function `next_Perfect_Square` takes an integer `n` as input and returns the next perfect square greater than `n`.

The function starts by calculating the integer square root of `n` and adding 1 to it. This is because the square root of `n` is the maximum possible integer that can be the square root of a perfect square less than `n`.

Then, it enters a loop where it calculates the square of the current integer `i` and checks if it is greater than `n`. If it is, the function returns the square as the next perfect square greater than `n`.

If the square is not greater than `n`, the function increments `i` by 1 and repeats the process until it finds the next perfect square greater than `n`.

The unit test `assert next_Perfect_Square(35) == 36` ensures that the function works correctly. It checks that the function returns 36, which is the next perfect square greater than 35.