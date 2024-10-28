        if (n < 1) return 0;
        int[] fib4_table = new int[n + 1];
        fib4_table[0] = 0;
        fib4_table[1] = 0;
        fib4_table[2] = 2;
        fib4_table[3] = 0;

        for (int i = 4; i <= n; i++) {
            fib4_table[i] = fib4_table[i - 1] + fib4_table[i - 2] + fib4_table[i - 3] + fib4_table[i - 4];
        }

        return fib4_table[n];
    }
}

