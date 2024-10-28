        int a = 0;
        int b = 1;
        for (int i = 0; i < n; i++) {
            int c = a + b;
            if (c % 2 == 0) {
                c += 1;
            }
            a = b;
            b = c;
        }
        return c;
    }
}

