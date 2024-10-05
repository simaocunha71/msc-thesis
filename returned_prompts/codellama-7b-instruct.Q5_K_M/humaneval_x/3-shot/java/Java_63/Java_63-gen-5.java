        if (n <= 1) return 0;

        int a = 0;
        int b = 0;
        int c = 1;

        for (int i = 0; i < n - 3; i++) {
            a = b;
            b = c;
            c = a + b + c;
        }
        return c;
    }
}

