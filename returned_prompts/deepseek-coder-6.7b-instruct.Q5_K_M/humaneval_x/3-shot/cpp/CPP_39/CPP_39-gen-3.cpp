    int fib_1 = 2;
    int fib_2 = 3;
    int fib_n = 5;
    int count = 3;
    if (n == 1) return 2;
    if (n == 2) return 3;
    if (n == 3) return 5;
    while(count < n){
        int fib_old = fib_2;
        fib_2 = fib_n;
        fib_1 = fib_old;
        fib_n = fib_1 + fib_2;
        count++;
    }
    return fib_n;
}


