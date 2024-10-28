    if(n == 0) return 0;
    if(n == 1) return 0;
    if(n == 2) return 1;

    int[] fib = new int[n+1];
    fib[0] = 0;
    fib[1] = 0;
    fib[2] = 1;

    for(int i=3; i <= n; i++){
        fib[i] = fib[i-1] + fib[i-2] + fib[i-3];
    }

    return fib[n];
}
}

This problem can be solved by using a dynamic programming approach. The time complexity of the solution is O(n) and the space complexity is also O(n).
The solution starts by initializing an array fib of size n+1 to store the FibFib numbers. The array is initialized with the base cases fib[0] = 0, fib[1] = 0, and fib[2] = 1.
Then, a loop is used to compute the FibFib numbers from the 3rd to the nth. The i-th FibFib number is computed by adding the (i-1)-th, (i-2)-th, and (i-3)-th FibFib numbers.
Finally, the n-th FibFib number is returned.

The provided solution can be further optimized by using a constant space. This can be done by keeping track of only the last three FibFib numbers at any given time. Here is the optimized solution:

```java
public int fibfib(int n) {
    if (n == 0) return 0;
    if (n == 1) return 0;
    if (n == 2) return 1;

    int a = 0, b = 0, c = 1;
    int d;

    for (int i = 3; i <= n; i++) {
        d = a + b + c;
        a = b;
        b = c;
        c = d;
    }

    return c;
}
```

This optimized solution has a space complexity of O(1), which is a significant improvement over the previous solution.
In this solution, the variables a,