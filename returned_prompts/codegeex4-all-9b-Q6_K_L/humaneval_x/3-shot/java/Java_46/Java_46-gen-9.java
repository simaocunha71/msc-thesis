        int[] fib4 = {0, 0, 2, 0};
        if (n < 0) return -1;
        if (n < 4) return fib4[n];

        for (int i = 4; i <= n; i++) {
            fib4[i % 4] = fib4[(i - 1) % 4] + fib4[(i - 2) % 4] + fib4[(i - 3) % 4] + fib4[(i - 4) % 4];
        }
        return fib4[n % 4];
    }
}

