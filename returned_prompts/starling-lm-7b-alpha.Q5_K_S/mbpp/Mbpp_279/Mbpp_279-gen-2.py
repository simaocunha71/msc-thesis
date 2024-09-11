```
def is_num_decagonal(n):
    # A decagonal number is a polygonal number that is formed from a decagon.
    # The formula for decagonal numbers is n*(n+1) / 10 + 1
    decagonal_number = (n * (n + 1)) // 10 + 1
    return decagonal_number
```

In this function, we define a function called `is_num_decagonal` that takes a parameter `n`, which represents the position of the decagonal number we want to find. We use a formula for decagonal numbers to calculate the decagonal number at position `n` and return it. The formula for decagonal numbers is `(n * (n + 1)) // 10 + 1`.

To test the function, you can use the `assert` statement to check if the function returns the correct result for a given input. In this case, we assert that `is_num_decagonal(3)` should equal `27`.

By running the code, the function will calculate the decagonal number at position `n` and return it. If the assertion is true, the function is correct and the test passes. Otherwise, an error message will be raised, indicating that the function is incorrect.

This function can be used to find the nth decagonal number by passing the desired position `n` as an argument to the function.

Here are some examples of decagonal numbers:

- The first decagonal number is 1.
- The second decagonal number is 2 + 1 = 3.
- The third decagonal number is 3 + 2 = 6.
- The fourth decagonal number is 4 + 3 = 10.
- The fifth decagonal number is 5 + 4 = 15.
- The sixth decagonal number is 6 + 5 = 22.
- The seventh decagonal number is 7 + 6 = 30.
- The eighth decagonal number is 8 + 7 = 42.
- The ninth decagonal number is 9 + 8 = 56.
- The tenth decagonal number is 10 + 9 = 72.

The function correctly calculates the