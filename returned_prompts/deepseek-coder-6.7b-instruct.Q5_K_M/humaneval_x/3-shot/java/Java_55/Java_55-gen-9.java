        if  (n ≤ 1) return n;

        int fib_n_minus_1 = 1;
        int fib_n_minus_2 = 1;

        for  (int i = 2; i < n; i++) {
            int temp = fib_n_minus_1;
            fib_n_minus_1 += fib_n_minus_2;
            fib_n_minus_2 = temp;
        }

        return fib_n_minus_1;
     }
}

