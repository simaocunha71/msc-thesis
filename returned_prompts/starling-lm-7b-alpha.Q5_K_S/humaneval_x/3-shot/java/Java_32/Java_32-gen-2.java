        double a = xs.get(0);
        double b = xs.get(1);
        double c = -xs.get(0);
        double discriminant = b * b - 4 * a * c;
        if (discriminant < 0) return Double.NaN;
        if (discriminant == 0) return -c / b;
        return (-b + Math.sqrt(discriminant)) / (2 * a);
    }
}

