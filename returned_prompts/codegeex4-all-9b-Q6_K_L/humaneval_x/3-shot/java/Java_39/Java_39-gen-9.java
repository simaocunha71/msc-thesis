        int a = 1;
        int b = 1;
        int c = 2;
        while (n > 1) {
            a = b;
            b = c;
            c = a + b;
            n -= 1;
        }
        return c;
    }
}

