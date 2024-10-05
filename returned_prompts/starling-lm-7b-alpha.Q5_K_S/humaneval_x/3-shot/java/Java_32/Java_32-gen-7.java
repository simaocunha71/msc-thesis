        double a = xs.get(0);
        double b = xs.get(1);
        double c = -xs.get(0);
        double discriminant = Math.sqrt(b * b - 4 * a * c);
        return (-b + discriminant) / (2.0 * a);
    }
}


