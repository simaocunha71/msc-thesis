    double x = 0;
    double eps = 0.000000000001;
    int i;
    int len = xs.size();
    if (len <= 1) return -1;
    for (i=1;i<len;i++)
    {
        x = x - xs[i]/xs[i-1];
    }
    return x;
}

double find_min(vector<double> xs){
    /*
    >>> find_min([2, -3, 4]) # f(x) = 2 + 3x - 4x^2
    1.0
    >>> find_min([1, 2]) # f(x) = 1 + 2x
    -0.5
    >>> find_min([-6, 11, -6, 1]) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3 
    1.0
    */

    double x = 0;
    double eps = 0.000000000001;
    int i;
    int len = xs.size();
    if (len <= 1) return -1;
    for (i=1;i<len;i++)
    {
        x = x - xs[i]/xs[i-1];
    }
    double min = poly(xs, x);
    for (i=0;i<len;i++)
    {
        if (fabs(min) > fabs(poly(xs, x-eps))){
            min = poly(xs, x-eps);
            x = x - eps;
        }
        if (fabs(min) > fabs(poly(xs, x+eps))){
            min = poly(xs, x+eps);
            x = x + eps;
        }
    }
    return x;
}

double find_max(vector<double> xs){
    /*
    >>> find_max([2, -3, 4])