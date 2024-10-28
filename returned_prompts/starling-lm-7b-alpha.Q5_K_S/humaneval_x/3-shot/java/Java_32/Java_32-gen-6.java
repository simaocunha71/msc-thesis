        int n = xs.size() / 2;
        if (n == 0) return 0;
        double a = xs.get(n);
        double b = xs.get(n - 1);
        double x = -b / a;
        return poly(xs, x);
    }
}



```