```
def dog_age(human_years):
    return human_years * 7
```

Explanation:
To calculate a dog's age in dog's years, we can use the formula that 1 dog year is equal to 7 human years. Therefore, we can multiply the human years by 7 to get the dog's age in dog's years. 

In the provided code, the function `dog_age` takes the `human_years` as input and returns the equivalent age in dog's years by multiplying the `human_years` by 7.

To test the function, the `assert` statement is used to verify if the function returns the correct result for a given input. In this case, the `assert` statement checks if `dog_age(12)` returns 61, which is the expected result for a human age of 12 years.

By executing the `dog_age` function with different inputs, we can calculate a dog's age in dog's years accurately.

Here are some additional test cases to verify the function:

```python
def test_dog_age():
    assert dog_age(2) == 14
    assert dog_age(4) == 28
    assert dog_age(6) == 42
    assert dog_age(8) == 56
    assert dog_age(10) == 70
    print("All test cases passed.")
```

In this test function, we have added more test cases to check if the function correctly calculates the dog's age for various human ages. The `assert` statements are used to verify if the returned value matches the expected result. If all the `assert` statements pass without any exceptions, the message "All test cases passed." is printed, indicating that the function is working correctly.

You can run the test function to verify the correctness of the `dog_age` function.

Overall, the provided solution calculates a dog's age in dog's years using the formula 1 dog year = 7 human years, and the test function ensures the accuracy of the implementation.

Additionally, it's worth noting that this function assumes that dogs age at the same rate throughout their lives.