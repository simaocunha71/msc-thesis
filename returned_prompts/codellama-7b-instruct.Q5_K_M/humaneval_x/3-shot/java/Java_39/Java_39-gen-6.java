        if (n < 1) return 0;
        int a = 0, b = 1;
        while (n-- > 1) {
            int c = a + b;
            a = b;
            b = c;
        }
        for (int i = 2; i * i <= b; i++) {
            if (b % i == 0) return primeFib(n + 1);
        }
        return b;
    }
}

