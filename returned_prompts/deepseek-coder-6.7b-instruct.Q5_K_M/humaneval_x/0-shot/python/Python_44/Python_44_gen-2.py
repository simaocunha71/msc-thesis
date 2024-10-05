
```python
def change_base(x: int, base: int):
    if x < base:
        return str(x)
    else:
        return change_base(x // base, base) + str(x % base)
```

This function works by recursively dividing the input number by the new base, and then converting the remainder to a string. The result of this recursive process is the new representation of the number in the given base.

This function does not use any Python libraries or built-in functions that directly convert numbers between bases. Instead, it manually calculates the base conversion using integer division and modulus operations, which are fundamental aspects of number base conversion.

To test the function, you can use the doctest module. Here's how you can do it:

```python
import doctest
doctest.testmod()
```

If there are no test failures, the function is working as expected.

This function can be used to convert any integer to any base between 2 and 9. For bases greater than 9, you would need to define your own mapping of numbers to characters, as there are no built-in ways to convert to bases greater than 10.

Please note that the function does not handle negative integers. If you want to support negative integers, you would need to modify the function to handle this case separately.
