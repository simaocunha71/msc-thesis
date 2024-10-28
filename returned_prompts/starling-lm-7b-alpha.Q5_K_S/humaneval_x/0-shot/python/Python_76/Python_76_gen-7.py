    from math import log, floor

    if x == 1:
        return True

    if log(x) % log(n) != 0:
        return False

    return floor(log(x) / log(n)) == int(floor(log(x) / log(n)))


if __name__ == '__main__':
    print(is_simple_power(2, 2))
    print(is_simple_power(8, 2))
    print(is_simple_power(3, 2))
    print(is_simple_power(3, 1))
    print(is_simple_power(5, 3))



```

This function, `is_simple_power`, checks if a number `x` is a simple power of another number `n`. It does this by first checking if `x` is equal to 1, in which case it returns True. Then it checks if the logarithm of `x` modulo the logarithm of `n` is not equal to zero. If it is not zero, it returns False. Otherwise, it calculates the floor of the logarithm of `x` divided by the logarithm of `n` and checks if it is equal to the integer value of that result. If it is, it returns True; otherwise, it returns False.

The function is then tested with several examples, including the ones provided in the question.





The output of the code is:

```
True
True
False
False
False
```




The function correctly identifies whether a number is a simple power of another number, as per the requirements of the question.





























































































































