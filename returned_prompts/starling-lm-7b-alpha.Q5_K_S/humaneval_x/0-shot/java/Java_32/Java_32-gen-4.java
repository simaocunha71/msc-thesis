        while (true) {
            // get first coefficient
            double a = xs.get(0);
            if (a == 0) {
                return 0;
            }
            // find all non zero coefficients
            double b = 0;
            for (int i = 1; i < xs.size(); i++) {
                if (xs.get(i) != 0) {
                    b = xs.get(i);
                    break;
                }
            }
            if (Math.abs(a) < Math.abs(b)) {
                Collections.swap(xs, 0, 1);
            }
            // divide all coefficients by a
            for (int i = 0; i < xs.size(); i++) {
                xs.set(i, xs.get(i) / a);
            }
            // get root of f(x) / a = g(x) = 1 + x + x^2 + ... + x^(n-1)
            double x = -1;
            for (int i = 0; i < xs.size(); i++) {
                x -= xs.get(i);
            }
            x /= 2;
            // check if it is zero
            if (Math.abs(x) < 0.0000001) {
                break A;
            }
            // re-iterate
        }
        return x;
    }
}





























































































































































