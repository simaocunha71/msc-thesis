        int fib0 = 0, fib1 = 0, fib2 = 1;
        for (int i = 3; i <= n; i++) {
            int fibi = fib0 + fib1 + fib2;
            fib0 = fib1;
            fib1 = fib2;
            fib2 = fibi;
        }
        return fib2;
    }
}

