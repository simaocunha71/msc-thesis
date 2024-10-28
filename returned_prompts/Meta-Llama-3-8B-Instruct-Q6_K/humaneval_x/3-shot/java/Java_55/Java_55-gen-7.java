        if (n <= 1) {
            return n;
        }
        int[] fib_sequence = new int[n + 1];
        fib_sequence[0] = 0;
        fib_sequence[1] = 1;
        for (int i = 2; i <= n; i++) {
            fib_sequence[i] = fib_sequence[i - 1] + fib_sequence[i - 2];
        }
        return fib_sequence[n];
    }
}

