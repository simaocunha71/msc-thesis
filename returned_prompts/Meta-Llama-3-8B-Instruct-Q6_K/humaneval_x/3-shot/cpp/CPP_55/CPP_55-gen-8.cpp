    if (n==1)
    return 1;
    else if (n==2)
    return 1;
    else
    return fib(n-1)+fib(n-2);
} // This function is not efficient for large values of n
// We need to use memoization or dynamic programming for this.


