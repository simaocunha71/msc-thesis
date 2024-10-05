        if (n <= 1) {
            return n;
        }
        int a = 0, b = 1, result = 0;
        for (int i = 2; i <= n; i++) {
            result = a + b;
            a = b;
            b = result;
        }
        return result;
    }
}

Solutions:

1.  This solution calculates the nth Fibonacci number using a for loop. It initializes two variables `a` and `b` to 0 and 1 respectively, and a variable `result` to 0. Then it iterates from 2 to `n`, updating the values of `a` and `b` to be the sum of the previous two values, and updating `result` to be the current value of `a`. Finally, it returns the value of `result`.
2.  This solution calculates the nth Fibonacci number using recursion. It defines a function `fib` that takes an integer `n` as input, and returns the `n`-th Fibonacci number. If `n` is 0 or 1, it returns `n`. Otherwise, it calls itself with `n-1` and `n-2` as arguments, and returns the sum of the results.
3.  This solution calculates the nth Fibonacci number using dynamic programming. It defines a function `fib` that takes an integer `n` as input, and returns the `n`-th Fibonacci number. It initializes an array `dp` of size `n+1` with all elements set to 0, and sets `dp[1]` and `dp[2]` to 1. Then it iterates from 3 to `n`, updating `dp[i]` to be the sum of `dp[i-1]` and `dp[i-2]`. Finally, it returns `dp[n]`.
4.  This solution calculates the nth Fibonacci number using matrix exponentiation. It defines a function `fib` that takes an integer `n` as input, and returns the `n`-th Fibonacci number. It defines a matrix `M` with two elements, and calculates the power of `M` using exponentiation by squaring. Then it extracts the top-left element of the resulting matrix, which is the `n`-th Fibonacci number. This solution has a time complexity of O(log n).

```
Solution:
public int fib(int n) {
    if (n <= 1