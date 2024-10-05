        if (n == 0 || n == 1) {
            return 0;
        } else if (n == 2) {
            return 2;
        } else if (n == 3) {
            return 0;
        } else {
            int a = 0;
            int b = 2;
            int c = 0;
            for (int i = 4; i <= n; i++) {
                int temp = b;
                b = c;
                c = a + b + c;
                a = temp;
            }
            return b;
        }
    }
}

