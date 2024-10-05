    if (n<2)
    return n;
    int fib_n_1=fib(n-1);
    int fib_n_2=fib(n-2);
    return fib_n_1+fib_n_2;
} // this is not efficient for large n, because it does a lot of repeated computation.
// we can use a more efficient method like dynamic programming.
// with dynamic programming, we can store the results of subproblems and reuse them instead of recomputing them. 

