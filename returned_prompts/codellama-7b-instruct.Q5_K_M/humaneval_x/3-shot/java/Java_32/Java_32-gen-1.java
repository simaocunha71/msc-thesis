        double x1 = -xs.get(0) / xs.get(1);
        double x2 = -xs.get(0) / (xs.get(1) + xs.get(2));
        double x3 = -xs.get(0) / (xs.get(1) + xs.get(2) + xs.get(3));

        if (x1 >= x2 && x1 >= x3) return x1;
        if (x2 >= x1 && x2 >= x3) return x2;
        if (x3 >= x1 && x3 >= x2) return x3;

        return 0.0;
    }
}

