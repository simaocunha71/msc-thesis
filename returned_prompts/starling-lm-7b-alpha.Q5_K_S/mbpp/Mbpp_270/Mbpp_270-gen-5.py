"""
def sum_even_and_even_index(input_list):
    summ = 0
    for i in range(0, len(input_list), 2):
        if input_list[i] % 2 == 0:
            summ += input_list[i]
    return summ
"""

def sum_even_and_even_index(input_list):
    summ = 0
    for i in range(0, len(input_list), 2):
        if input_list[i] % 2 == 0:
            summ += input_list[i]
    return summ


def test_sum_even_and_even_index():
    assert sum_even_and_even_index([5, 6, 12, 1, 18, 8]) == 30


test_sum_even_and_even_index()


# Made By Mostafa_Khaled
```

The code above defines a function called `sum_even_and_even_index` that takes in a list as an argument. It initializes a variable `summ` to 0, which will store the sum of even numbers at even positions.

The function then uses a `for` loop to iterate through the input list with a step size of 2. This ensures that only even positions are considered. Inside the loop, the function checks if the current element at index `i` is even by using the modulo operator (`%`) to check if the remainder of the division by 2 is 0. If it is, the element is added to the `summ` variable.

Finally, the function returns the calculated sum.

The provided assert statement is used to test the function and ensure that it returns the expected result for the given input list `[5, 6, 12, 1, 18, 8]`, which should be 30.

After defining the function and the assert statement, the code calls the `test_sum_even_and_even_index` function to run the test and verify that the function is working correctly.

This solution allows you to find the sum of even numbers at even positions in a list using the `sum