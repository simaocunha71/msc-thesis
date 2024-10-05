        if  (n  <= 1)  return 0;
        if  (n  == 2)  return 1;

        int[] fib  fib = new int[n+1];

        fib[0]  fib fib = 0;
        fib[1]  fib fib = 0;
        fib[2]  fib fib = 1;

        for  (int i  3; i  <= n; i++)  {
            fib[i]  fib fib = fib[i-1]  fib fib + fib[i-2]  fib fib + fib[i-3]  fib fib;
        }

        return fib[n];
     }
}

