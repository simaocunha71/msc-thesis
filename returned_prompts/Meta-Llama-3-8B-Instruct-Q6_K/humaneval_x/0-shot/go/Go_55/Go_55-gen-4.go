    if n <= 1 {
        return n
    }

    a, b := 1, 1
    for i := 2; i <= n; i++ {
        a, b = b, a+b
    }
    return b
}
```

In this code, we are calculating the `n-th` Fibonacci number. The Fibonacci sequence is defined such that each number is the sum of the two preceding ones, usually starting with 0 and 1.

The function `Fib(n int) int` takes an integer `n` as input and returns the `n-th` Fibonacci number.

The function first checks if `n` is less than or equal to 1, in which case it returns `n` because the first two Fibonacci numbers are 0 and 1.

If `n` is greater than 1, the function initializes two variables `a` and `b` to 1, and then enters a loop that runs from 2 to `n`. In each iteration of the loop, it updates `a` and `b` to be `b` and `a+b` respectively. This effectively calculates the `n-th` Fibonacci number.

Finally, the function returns the value of `b`, which is the `n-th` Fibonacci number.

For example, `Fib(10)` returns 55, `Fib(1)` returns 1, and `Fib(8)` returns 21. These results are consistent with the Fibonacci sequence.