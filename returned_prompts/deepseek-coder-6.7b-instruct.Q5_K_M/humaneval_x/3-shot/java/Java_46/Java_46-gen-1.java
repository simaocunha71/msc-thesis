        if  (n < 2) return 0;
        if  (n == 2) return 2;
        if  (n == 3) return 0;

        int[] fib  n%4  new int[n+1];
        fib[0] = 0;
        fib[1] = 0;
        fib[2] = 2;
        fib[3] = 0;

        for  (int i = 4; i <= n; i++) {
            fib[i % 4] = fib[0] + fib[1] + fib[2] + fib[3];
        }

        return fib[n % 4];
     }
}

