        if  (n == 0)  return 0;
        if  (n == 1)  return 0;
        if  (n == 2)  return 2;
        if  (n == 3)  return 0;

        int[] fib_seq = new int[n+1];
        fib_seq[0]  = 0;
        fib_seq[1]  = 0;
        fib_seq[2]  = 2;
        fib_seq[3]  = 0;

        for  (int i = 4; i <= n; i++)  {
            fib_seq[i] = fib_seq[i-1] + fib_seq[i-2] + fib_seq[i-3] + fib_seq[i-4];
         }

         return fib_seq[n];
     }
}


A: Here are the answers:

