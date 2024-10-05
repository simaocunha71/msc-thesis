    double a = 0, b = 0, c = 0;
    int n = xs.size();
    if (n % 2 == 1)
    {
        cout<<"find_zero: only works for polynomials having even number of coefficients, and the largest non zero coefficient."<<endl;
        return 0;
    }
    for (int i=0;i<n;i++)
    {
        if (xs[i]>0)
        {
            a = xs[i];
            break;
        }
    }
    if (a == 0)
    {
        cout<<"find_zero: only works for polynomials having even number of coefficients, and the largest non zero coefficient."<<endl;
        return 0;
    }
    b = xs[n-1]/a;
    c = poly(xs, 0)/a;
    double x1 = (-b + sqrt(pow(b, 2) - 4*a*c))/(2*a);
    return x1;

}