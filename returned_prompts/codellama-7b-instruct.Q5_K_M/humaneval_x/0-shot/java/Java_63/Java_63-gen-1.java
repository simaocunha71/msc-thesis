        if (n <= 2) {
            return n;
        }
        int a = 0, b = 0, c = 1;
        for (int i = 3; i <= n; i++) {
            a = b;
            b = c;
            c = a + b + c;
        }
        return c;
    }
}
