        if (n == 0 || n == 1) return 0;
        if (n == 2) return 1;
        int fib_n_minus_3 = 0;
        int fib_n_minus_2 = 1;
        int fib_n_minus_1 = 1;
        int fib_n = 0;
        for (int i = 3; i <= n; i++) {
            fib_n = fib_n_minus_1 + fib_n_minus_2 + fib_n_minus_3;
            fib_n_minus_3 = fib_n_minus_2;
            fib_n_minus_2 = fib_n_minus_1;
            fib_n_minus_1 = fib_n;
        }
        return fib_n;
    }
}

