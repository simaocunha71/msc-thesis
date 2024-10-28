    double x_0;
    double x_1;
    int i;
    int n;
    n=xs.size();
    if (n%2==0)
    x_0=xs[n/2-1];
    else
    x_0=xs[n/2];

    x_1=xs[n/2];
    double epsilon=0.0000001;
    double diff=x_1-x_0;
    double x_k;
    double x_k1;
    double y_k;
    double y_k1;
    for (i=0;i<1000;i++)
    {
        x_k=x_0-diff/poly(xs,x_0);
        x_k1=x_0-diff/poly(xs,x_k);
        if (x_k1==x_k)
        break;
        diff=x_k1-x_k;
    }
    return x_k1;
}


