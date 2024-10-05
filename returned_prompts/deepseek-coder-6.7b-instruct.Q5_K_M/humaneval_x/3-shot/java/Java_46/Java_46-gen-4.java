        if (n < 4) {
            return n == 3 ? 0 : n;
        }

        int a = 0, b = 0, c = 2, d = 0;
        int result = 0;

        for (int i = 4; i <= n; i++) {
            result = a + b + c + d;
            a = b;
            b = c;
            c = d;
            d = result;
        }

        return result;
    }
}

