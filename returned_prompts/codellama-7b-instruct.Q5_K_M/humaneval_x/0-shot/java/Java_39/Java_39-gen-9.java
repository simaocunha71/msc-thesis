        int a = 0, b = 1, c = 1;

        for (int i = 0; i < n; i++) {
            c = a + b;
            a = b;
            b = c;
            for (int j = 2; j <= Math.sqrt(c); j++) {
                if (c % j == 0) {
                    continue A;
                }
            }
        }
        return c;
    }
}

