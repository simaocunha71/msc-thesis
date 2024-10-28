def sum_to_n(n: int):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total
    



This function takes an integer `n` as an argument and returns the sum of all integers from 1 to `n`. It uses a for loop to iterate over the range from 1 to `n` (inclusive), adding each number to a running total. The function returns the final total.

The function is tested with different inputs to ensure it produces the correct output. For example, `sum_to_n(30)` should return `465`, and `sum_to_n(100)` should return `5050`. These tests ensure that the function is working correctly for different values of `n`.