        int a = 0;
        int b = 0;
        int c = 2;
        int d = 0;

        for (int i = 0; i < n; i++) {
            int temp = d;
            d = c;
            c = a + b + c;
            a = b;
            b = temp;
        }
        return d;
    }
}

