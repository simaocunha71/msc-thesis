        if  (n ≤ 1) return n;
        int a = 0;
        int b = 1;

        for  (int i = 2; i ≤ n; i++) {
            int temp = a + b;
            a = b;
            b = temp;
        }
        return b;
     }
}

