        int a = 0, b = 1, c = 1, d = 0;
        for (int i = 0; i < n; i++) {
            c = (a + b) % 1000000007;
            d = b;
            b = a;
            a = c;
        }
        return (d + c) % 1000000007;
    }
}

