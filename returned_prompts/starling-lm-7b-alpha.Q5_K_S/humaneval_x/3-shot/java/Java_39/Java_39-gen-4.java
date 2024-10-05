        int a = 0;
        int b = 1;
        int c = 0;
        int tmp;

        while (c < n) {
            tmp = a;
            a = b;
            b = c;
            c = a + b;

            if (c % 2 == 0) continue;
            for (int i = 2; i * i <= c; ++i) {
                if (c % i == 0) {
                    continue A;
                }
            }
            return c;
        }
        return -1;
    }
}

