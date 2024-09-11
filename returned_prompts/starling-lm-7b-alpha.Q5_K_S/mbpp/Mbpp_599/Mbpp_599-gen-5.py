```
def sum_average(n):
    sum=0
    for i in range(1,n+1):
        sum+=i
    return sum,sum/n
```

The above code defines a function `sum_average` which takes an argument `n`. It initializes a variable `sum` to 0. Then it uses a `for` loop to iterate over the range from 1 to `n+1`. In each iteration, it adds the current number to the `sum` variable. After the loop is finished, it returns a tuple containing the sum of the first `n` natural numbers and the average of the first `n` natural numbers.

To test the function, you can use the `assert` statement to check if the function returns the correct result for a given input. In this case, the `assert` statement checks if `sum_average(10)` returns the tuple `(55, 5.5)`, which is the expected result.

To use the function, you can simply call it with the desired value of `n` as the argument. For example, `sum_average(10)` will return the sum and average of the first 10 natural numbers.

Overall, this function provides a simple and efficient way to calculate the sum and average of the first `n` natural numbers.

Here's a step-by-step explanation of the code:

1. Define a function `sum_average` that takes an argument `n`.
2. Initialize a variable `sum` to 0. This variable will store the sum of the first `n` natural numbers.
3. Use a `for` loop to iterate over the range from 1 to `n+1`. In each iteration, add the current number to the `sum` variable.
4. After the loop is finished, return a tuple containing the `sum` variable and the average of the first `n` natural numbers (which is calculated by dividing the `sum` by `n`).
5. To test the function, use the `assert` statement to check if the function returns the correct result for a given input (in this case, `sum_average(10)` should return `(55, 5.5)`).
6. To use the function,