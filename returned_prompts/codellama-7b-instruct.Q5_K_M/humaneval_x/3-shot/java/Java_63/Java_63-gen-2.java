        if (n == 0) return 0;
        if (n == 1) return 0;
        if (n == 2) return 1;

        int a = 0;
        int b = 0;
        int c = 1;

        for (int i = 3; i <= n; i++) {
            a = b;
            b = c;
            c = a + b + c;
        }
        return c;
    }
}

