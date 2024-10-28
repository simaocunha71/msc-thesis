        if (n <= 1) return n;

        int fib = 2;
        int fib_prev = 1;
        int fib_prev_prev = 0;

        while (true) {
            fib = fib_prev + fib_prev_prev;
            fib_prev_prev = fib_prev;
            fib_prev = fib;

            if (fibFib(fib) == 1) return fib;
        }
    }
}

