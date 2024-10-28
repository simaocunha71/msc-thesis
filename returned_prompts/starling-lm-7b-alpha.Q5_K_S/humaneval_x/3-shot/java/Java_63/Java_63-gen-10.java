        if (n == 0) return 0;
        if (n == 1) return 0;
        if (n == 2) return 1;

        int[] fib_cache = new int[n + 1];
        fib_cache[0] = 0;
        fib_cache[1] = 0;
        fib_cache[2] = 1;

        for (int i = 3; i <= n; i++) {
            fib_cache[i] = fib_cache[i - 1] + fib_cache[i - 2] + fib_cache[i - 3];
        }
        return fib_cache[n];
    }
}

