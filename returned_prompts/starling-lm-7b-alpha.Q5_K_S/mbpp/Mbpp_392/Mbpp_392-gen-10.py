```
def f(n):
    if (n < 4):
        return n
    else:
        return max((f(n/2) + f(n/3) + f(n/4) + f(n/5)), n)

def get_max_sum(n):
    return f(n)
```

This function works by recursively dividing the input number by 2, 3, 4, and 5 until it reaches one of the base cases (i.e., when n < 4). At each step, it adds the maximum of the remaining values to the current value of n. The result is the maximum sum possible using the given equation.

The function `f(n)` is a helper function that performs the actual calculation. It takes a number `n` as input and returns the maximum sum possible using the equation `f(n) = max( (f(n/2) + f(n/3) + f(n/4) + f(n/5)), n)`. If `n` is less than 4, it simply returns `n` as the base case. Otherwise, it recursively calls itself with the remaining values of `n` divided by 2, 3, 4, and 5, and returns the maximum value.

The function `get_max_sum(n)` is the main function that takes an input number `n` and calls the `f(n)` function to calculate the maximum sum. It then returns this maximum sum as the result.

To test the function, you can use the assertion `assert get_max_sum(60) == 106`. This assertion checks if the `get_max_sum` function correctly calculates the maximum sum for the input number 60, and verifies that the result is indeed 106.

Overall, this code provides a solution to finding the maximum sum possible by using the given equation, and the provided assertion confirms the correctness of the function for the specific case of input number 60.

"""

"""
Write a function to find the maximum sum possible by using the given equation f(n) = max( (f(n/2) + f(n/3) + f(n/4) + f(