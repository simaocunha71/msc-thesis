    double y = pow(n, 0.5);
    return (y == int(y) && pow(y, 2) == x);
} // Note: This code is not suitable for large numbers due to the precision of float in C++. For large numbers, it's better to use logarithmic approach.