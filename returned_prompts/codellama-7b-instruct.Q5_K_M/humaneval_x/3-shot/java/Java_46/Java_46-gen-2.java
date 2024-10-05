        int a = 0;
        int b = 0;
        int c = 2;
        int d = 0;

        for (int i = 0; i < n; i++) {
            int t = a;
            a = b;
            b = c;
            c = d;
            d = t + b + c + d;
        }
        return d;
    }
}

