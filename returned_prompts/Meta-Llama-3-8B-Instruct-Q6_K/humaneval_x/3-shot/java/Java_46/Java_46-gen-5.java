        if (n <= 1) {
            return 0;
        } else if (n == 2) {
            return 2;
        } else {
            int[] fib4_sequence = new int[n + 1];
            fib4_sequence[1] = 0;
            fib4_sequence[2] = 2;
            for (int i = 3; i <= n; i++) {
                fib4_sequence[i] = fib4_sequence[i - 1] + fib4_sequence[i - 2] + fib4_sequence[i - 3] + fib4_sequence[i - 4];
            }
            return fib4_sequence[n];
        }
    }
}

