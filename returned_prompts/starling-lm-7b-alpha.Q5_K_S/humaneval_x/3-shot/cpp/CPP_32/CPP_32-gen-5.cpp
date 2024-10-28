    double x1, x2, x3, x4;
    x1 = (-xs[2] + sqrt(pow(xs[2], 2) - 4 * xs[0] * xs[3])) / (2 * xs[1]);
    x2 = (-xs[2] - sqrt(pow(xs[2], 2) - 4 * xs[0] * xs[3])) / (2 * xs[1]);
    x3 = x1 + x2;
    x4 = (xs[1] * x3 + xs[0]) / xs[3];
    return x4;
}


