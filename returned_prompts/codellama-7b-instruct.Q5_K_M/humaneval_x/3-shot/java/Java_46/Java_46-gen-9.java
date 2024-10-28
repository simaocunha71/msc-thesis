        int a = 0, b = 0, c = 1, d = 1;
        for (int i = 0; i < n - 1; i++) {
            a = b;
            b = c;
            c = d;
            d = a + b + c + d;
        }
        return d;
    }
}

