    int f1 = 0, f2 = 0, f3 = 2, f4 = 0, fib = 0;
    if (n == 0)
        return f1;
    if (n == 1)
        return f2;
    if (n == 2)
        return f3;
    if (n == 3)
        return f4;
    for (int i = 4; i <= n; i++)
    {
        fib = f1 + f2 + f3 + f4;
        f1 = f2;
        f2 = f3;
        f3 = f4;
        f4 = fib;
    }
    return fib;
}


