        if (n <= 1) return n;
        int a = 0, b = 0, c = 2;
        for (int i = 3; i <= n; i++) {
            a = b;
            b = c;
            c = a + b + c;
        }
        return c;
    }
}

