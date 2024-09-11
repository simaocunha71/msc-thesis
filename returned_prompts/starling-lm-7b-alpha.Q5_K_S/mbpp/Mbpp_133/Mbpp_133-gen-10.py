def sum_negativenum(numlist):
    return sum(i for i in numlist if i<0)




# Python program to test the above function
def test_sum_negativenum():
    assert sum_negativenum([2, 4, -6, -9, 11, -12, 14, -5, 17])==-32
    print("All tests passed")


test_sum_negativenum()


```
def sum_negativenum(numlist):
    return sum(i for i in numlist if i<0)
```

This function `sum_negativenum` takes a list of numbers as input and returns the sum of the negative numbers from the list. It uses a generator expression `(i for i in numlist if i<0)` to create an iterator that yields only the negative numbers from the input list. The `sum` function is then used to calculate the sum of these negative numbers.

In the provided test case, the function is called with the list `[2, 4, -6, -9, 11, -12, 14, -5, 17]`. The negative numbers in this list are `[-6, -9, -12, -5]`, and their sum is `-32`. This is confirmed by the assertion `assert sum_negativenum([2, 4, -6, -9, 11, -12, 14, -5, 17])==-32`, which checks if the function returns the expected result.

Finally, the function `test_sum_negativenum` is called to run all the tests and print a message if all the tests pass.

```python
def test_sum_negativenum():
    assert sum_negativenum([2, 4, -6, -9, 11, -12, 14, -5, 17])==-32
    print("All tests passed")
```

This function `test_sum_negativenum` is a separate test function that can be used to verify the correctness of the `sum_neg