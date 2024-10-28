        double a = xs.get(xs.size() - 1);
        if (a == 0) return 0;
        double b = xs.get(xs.size() - 2);
        double c = xs.get(xs.size() - 3);
        double d = poly(xs, -c / b);
        if (d == 0) return 0;
        return -a / d;
    }
}

