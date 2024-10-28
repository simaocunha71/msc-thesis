    double a=xs[0];
    double b=xs[1];
    double c=xs[2];
    double d=xs[3];
    if (xs.size()>4)
    {
        printf("Error. Only 4-degree polynomial is implemented. Try increasing number of coefficients.\n");
        exit(0);
    }
    if (a==0)
    {
        printf("Error. Polynomial is not defined. Try with non-zero coefficient.\n");
        exit(0);
    }
    if (b==0)
    {
        printf("Error. Polynomial is not defined. Try with non-zero coefficient.\n");
        exit(0);
    }
    if (c==0)
    {
        printf("Error. Polynomial is not defined. Try with non-zero coefficient.\n");
        exit(0);
    }
    if (d==0)
    {
        printf("Error. Polynomial is not defined. Try with non-zero coefficient.\n");
        exit(0);
    }
    double delta=b*b-4*a*c;
    double x1=-b/(2*a)+sqrt(delta)/(2*a);
    double x2=-b/(2*a)-sqrt(delta)/(2*a);
    if (x1<x2)
    {
        return x1;
    }
    else
    {
        return x2;
    }
}



