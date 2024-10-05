    double a = 0.0, b = 1.0, c = a;
    while(fabs(poly(xs, c)) > 0.00001){
        if(poly(xs, a) * poly(xs, c) < 0)
            b = c;
        else
            a = c;
        c = (a + b) / 2;
    }
    return c;
}


