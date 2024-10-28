        double a = xs.get(xs.size() - 1);
        double b = xs.get(xs.size() - 2);
        double c = 0;
        for (int i = xs.size() - 3; i >= 0; i--) {
            c = c * xs.get(i) + 1;
        }
        double x = (-b + Math.sqrt(b * b - 4 * a * c)) / (2 * a);
        return x;
    }
}

