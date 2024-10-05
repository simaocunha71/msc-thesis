        int a = 0, b = 0, c = 2;
        int result = 0;
        for (int i = 0; i < n; i++) {
            result = a + b + c;
            a = b;
            b = c;
            c = result;
        }
        return result;
    }
}

