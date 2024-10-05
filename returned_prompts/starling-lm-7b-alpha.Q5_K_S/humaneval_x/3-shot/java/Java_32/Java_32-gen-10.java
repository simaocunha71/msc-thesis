        double x1 = (-xs.get(1)) / xs.get(0);
        double x2 = (xs.get(2) * x1 + xs.get(0)) / (xs.get(1) * x1 + xs.get(0));
        return x2;
    }
}

