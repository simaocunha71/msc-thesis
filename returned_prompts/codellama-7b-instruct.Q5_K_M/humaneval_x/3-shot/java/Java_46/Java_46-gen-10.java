        int a = 0, b = 0, c = 2;
        for (int i = 3; i <= n; i++) {
            a = b;
            b = c;
            c = a + b + i - 4;
        }
        return c;
    }
}

