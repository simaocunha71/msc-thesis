        int a = 0;
        int b = 1;
        int result = 0;

        if (n <= 1) {
            result = n;
        } else {
            for (int i = 2; i <= n; i++) {
                result = a + b;
                a = b;
                b = result;
            }
        }
        return result;
    }
}

