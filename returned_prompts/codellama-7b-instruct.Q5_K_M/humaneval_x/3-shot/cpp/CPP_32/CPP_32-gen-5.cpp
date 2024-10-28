    int i,j,n;
    double x0,x1,x2;
    double y0,y1,y2;
    double x;

    n=xs.size();
    if (n%2==1)
    {
        printf("The input list must have even number of coefficients\n");
        return -1;
    }
    if (xs[n-1]!=0)
    {
        printf("The largest non zero coefficient must be zero\n");
        return -1;
    }
    x0=0;
    x1=xs[n-2];
    x2=xs[n-3];
    y0=1;
    y1=1;
    y2=1;

    for (i=0;i<n-4;i+=2)
    {
        x=x0-y0/(y2-y0)*(x2-x0);
        x0=x1;
        x1=x;
        x2=x0-y0/(y2-y0)*(x2-x0);
        y0=y1;
        y1=y2;
        y2=y0-y0/(y2-y0)*(y2-y0);
    }
    return x;
}


