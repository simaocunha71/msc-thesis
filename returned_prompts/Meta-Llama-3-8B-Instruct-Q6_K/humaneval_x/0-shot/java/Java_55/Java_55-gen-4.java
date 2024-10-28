        if (n == 1) {
            return 1;
        }
        if (n == 2) {
            return 1;
        }
        int a = 1, b = 1;
        for (int i = 3; i <= n; i++) {
            int temp = a + b;
            a = b;
            b = temp;
        }
        return b;
    }
} // This is a correct implementation of Fibonacci sequence using iterative method.

Explanation:

The Fibonacci sequence is a series of numbers where a number is the sum of the two preceding ones, usually starting with 0 and 1. In this implementation, the function `fib(int n)` returns the `n-th` Fibonacci number.

The base cases are handled separately. If `n` is 1 or 2, the function returns 1, as the 1st and 2nd Fibonacci numbers are 1.

For `n` greater than 2, the function uses an iterative approach to calculate the `n-th` Fibonacci number. It initializes two variables `a` and `b` to 1, which represent the first two Fibonacci numbers. Then, it enters a loop that runs from 3 to `n`. In each iteration, it calculates the `n-th` Fibonacci number as the sum of the previous two numbers (`a` and `b`), updates `a` and `b` to the previous two numbers, and continues until the loop ends.

The final result is the `n-th` Fibonacci number, which is stored in the variable `b`. The function returns this value.

This implementation has a time complexity of O(n) and a space complexity of O(1), making it efficient for calculating large Fibonacci numbers.