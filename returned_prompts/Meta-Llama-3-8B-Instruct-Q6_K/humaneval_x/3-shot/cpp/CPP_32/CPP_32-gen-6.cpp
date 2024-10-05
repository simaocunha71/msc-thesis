    double left = -10;
    double right = 10;
    double mid;
    double sum;
    int i;
    while (right-left > 1e-6)
    {
        mid = (left + right) / 2;
        sum = poly(xs, mid);
        if (sum > 0)
        {
            right = mid;
        }
        else
        {
            left = mid;
        }
    }
    return left;
}  // end of find_zero


