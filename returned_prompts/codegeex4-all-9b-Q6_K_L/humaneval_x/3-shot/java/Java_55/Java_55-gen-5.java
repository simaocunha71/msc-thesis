        if (n <= 2) return n;
        int a = 1, b = 1;
        for (int i = 3; i <= n; i++) {
            int tmp = b;
            b = a + b;
            a = tmp;
        }
        return b;
    }
}

