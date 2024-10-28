    double zero;
    double temp;
    zero = xs[xs.size()-1];
    for (int i = xs.size()-2; i >= 0; i-=2) {
        temp = xs[i];
        xs[i] = - (double)(zero/temp);
        zero = temp;
    }
    return poly(xs, 0);
}

double find_min(vector<double> xs){
    /*
    find_min(xs) finds minimum of a polynomial with coefficients given in xs.
    >>> round(find_min([1, 2]), 2) #f(x) = 1 + 2x 
    -0.5 
    >>> round(find_min([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3 
    1.0
    */
    double min;
    double temp;
    double zero;
    min = poly(xs, 0);
    zero = xs[xs.size()-1];
    for (int i = xs.size()-2; i >= 0; i-=2) {
        temp = xs[i];
        xs[i] = - (double)(zero/temp);
        zero = temp;
    }
    return poly(xs, min);
}

double derivative(vector<double> xs){
    /*
    derivative(xs) calculates the derivative of polynomial with coefficients given in xs.
    >>> round(derivative([1, 2]), 2) #f(x) = 1 + 2x 
    2.0 
    >>> round(derivative([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3 
    11.0
    */
    int n = xs.size();
    double ans =