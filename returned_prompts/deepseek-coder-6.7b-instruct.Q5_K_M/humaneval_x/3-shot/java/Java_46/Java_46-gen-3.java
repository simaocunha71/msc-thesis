        if  (n ≤ 1) return 0;
        if  (n ≤ 2) return 1;
        if  (n ≤ 3) return 1;

        int[] fib = new int[n+1];

        fib[0] = 0;
        fib[1] = 0;
        fib[2] = 1;
        fib[3] = 1;

        for  (int i = 4; i ≤ n; i++) {
            fib[i] = fib[i-1] + fib[i-2] + fib[i-3] + fib[i-4];
        }

        return fib[n];
    }
}

