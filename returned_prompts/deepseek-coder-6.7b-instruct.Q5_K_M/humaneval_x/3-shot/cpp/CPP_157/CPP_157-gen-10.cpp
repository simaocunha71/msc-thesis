    float max_side, square_sum;

    if (a > b && a > c) {
        max_side = a;
        square_sum = pow(b, 2) + pow(c, 2);
    } else if (b > a && b > c) {
        max_side = b;
        square_sum = pow(a, 2) + pow(c, 2);
    } else {
        max_side = c;
        square_sum = pow(a, 2) + pow(b, 2);
    }

    return fabs(pow(max_side, 2) - square_sum) < 0.00001;
}


