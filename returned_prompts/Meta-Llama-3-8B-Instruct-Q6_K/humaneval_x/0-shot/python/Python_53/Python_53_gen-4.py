    def add(x: int, y: int) -> int:
        return x + y
    # Test cases
    assert add(2, 3) == 5
    assert add(5, 7) == 12
    print("All test cases pass!")  # Output: All test cases pass!  # noqa: E302
    return add
```

In the code, we have a function `add` that takes two integers `x` and `y` and returns their sum. The function is decorated with a docstring that describes its purpose. The docstring is written in a specific format, with a triple quotes `"""..."""`, and includes a brief description of the function and some test cases.

The test cases are written using the `assert` statement, which checks if the result of the function call is equal to the expected value. If the result is not equal to the expected value, the `assert` statement will raise an `AssertionError`.

In this case, we have two test cases: `add(2, 3)` should return `5`, and `add(5, 7)` should return `12`. The function is tested using these test cases, and if all test cases pass, the function is considered correct.

Finally, we return the `add` function using the `return` statement. This allows the function to be called and used elsewhere in the code.