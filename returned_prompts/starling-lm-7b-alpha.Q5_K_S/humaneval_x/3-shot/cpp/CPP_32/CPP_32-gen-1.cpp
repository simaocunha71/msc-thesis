    int i;
    double a=xs[0];
    double b=xs[1];
    double c=xs[2];
    double x_minus_1 = (-c + sqrt(c * c - 4 * a * b)) / (2 * a);
    double x_minus_2 = (-c - sqrt(c * c - 4 * a * b)) / (2 * a);
    double x_minus_1_plus_minus_2 = (x_minus_1 + x_minus_2) / 2;
    return poly(xs, x_minus_1_plus_minus_2);
}



