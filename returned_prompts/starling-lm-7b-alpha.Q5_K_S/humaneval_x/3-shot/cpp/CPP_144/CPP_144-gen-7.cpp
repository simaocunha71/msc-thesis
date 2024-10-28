    int x_numerator=x[0]-'0';
    int x_denominator=x[2]-'0';
    int n_numerator=n[0]-'0';
    int n_denominator=n[2]-'0';
    int gcd_ab=(x_numerator*n_denominator)+(n_numerator*x_denominator);
    int gcd_de=x_denominator*n_denominator;
    if (gcd_ab%gcd_de!=0)
    return false;
    if (gcd_ab/gcd_de<x_numerator||gcd_ab/gcd_de<n_numerator)
    return false;
    return true;
}


