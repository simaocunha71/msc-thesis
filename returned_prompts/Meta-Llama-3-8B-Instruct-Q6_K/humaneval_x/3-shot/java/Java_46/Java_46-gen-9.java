        if (n <= 0) {
            return 0;
        }
        int[] fib4_values = new int[n + 1];
        fib4_values[1] = 0;
        fib4_values[2] = 2;
        fib4_values[3] = 0;

        for (int i = 4; i <= n; i++) {
            fib4_values[i] = fib4_values[i - 1] + fib4_values[i - 2] + fib4_values[i - 3] + fib4_values[i - 4];
        }
        return fib4_values[n];
    }
}

