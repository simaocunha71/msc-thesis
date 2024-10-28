    if (n <= 1) {
        return n;
    } else {
        return fib(n-1) + fib(n-2);
    }
}

// Note: This solution has exponential time complexity and is not efficient for large values of n.
// A more efficient solution would use dynamic programming to store and reuse previously computed Fibonacci numbers.

