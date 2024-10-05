        if (n < 4) {
            return n;
        }

        int[] fib = new int[n + 1];
        fib[0] = 0;
        fib[1] = 0;
        fib[2] = 2;
        fib[3] = 0;

        int a = 0;
        int b = 0;
        int c = 2;
        int d = 0;
        int k;

        for (int i = 4; i <= n; i++) {
            for (k = 0; k < i; k++) {
                a = b;
                b = c;
                c = d;
                d = a + b + c + d;
            }
            fib[i] = d;
        }

        return fib[n];
    }
}
