        if (n <= 0) {
            return 0;
        } else if (n == 1) {
            return 0;
        } else if (n == 2) {
            return 2;
        } else {
            int[] fib4 = new int[5];
            fib4[0] = 0;
            fib4[1] = 0;
            fib4[2] = 2;
            fib4[3] = 0;
            for (int i = 4; i <= n; i++) {
                fib4[i % 4] = fib4[(i - 1) % 4] + fib4[(i - 2) % 4] + fib4[(i - 3) % 4] + fib4[(i - 4) % 4];
            }
            return fib4[n % 4];
        }
    }
}

