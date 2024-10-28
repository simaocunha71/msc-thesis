        if (n <= 1) {
            return 0;
        }
        if (n == 2) {
            return 2;
        }
        int[] fib4_array = new int[5];
        fib4_array[1] = 0;
        fib4_array[2] = 2;
        fib4_array[3] = 0;
        for (int i = 4; i <= n; i++) {
            fib4_array[i % 4] = (fib4_array[(i - 1) % 4] + fib4_array[(i - 2) % 4] + fib4_array[(i - 3) % 4]);
        }
        return fib4_array[n % 4];
    }
}

