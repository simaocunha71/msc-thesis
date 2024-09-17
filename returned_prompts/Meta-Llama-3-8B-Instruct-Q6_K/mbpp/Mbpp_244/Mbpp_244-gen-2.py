```
def next_Perfect_Square(n):
    i = 1
    while True:
        if i * i > n:
            return i * i
        i += 1
```
This function works by iterating over perfect squares starting from 1. It checks if the current perfect square is greater than the given number. If it is, it returns the perfect square. If not, it increments the perfect square and continues the loop. This way, it finds the first perfect square greater than the given number. The unit test `assert next_Perfect_Square(35) == 36` confirms this. For example, `next_Perfect_Square(35)` returns `36` which is the next perfect square greater than `35`. 

The time complexity of this function is O(sqrt(n)) as it has to iterate over perfect squares up to `n` to find the next one. The space complexity is O(1) as it only uses a constant amount of space to store the current perfect square and the input number. 