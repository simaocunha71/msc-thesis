        int a = 0;
        int b = 0;
        int c = 2;
        int d = 0;

        for (int i = 0; i <= n; i++) {
            if (i == 0) {
                a = 0;
                b = 0;
            } else if (i == 1) {
                a = 0;
                b = 0;
            } else if (i == 2) {
                a = 2;
                b = 0;
            } else if (i == 3) {
                a = 0;
                b = 0;
            } else {
                a = b;
                b = c;
                c = d;
                d = a + b + c + d;
            }
        }
        return d;
    }
}

