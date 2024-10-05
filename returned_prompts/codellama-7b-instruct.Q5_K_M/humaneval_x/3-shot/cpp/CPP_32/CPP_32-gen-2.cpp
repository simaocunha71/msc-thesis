    double x0=0;
    double x1=1;
    double x2;
    double f0=poly(xs,x0);
    double f1=poly(xs,x1);
    while (abs(f1)>0.000001)
    {
        x2=(x0-f0*x1/(f1-f0))/2;
        x0=x1;
        x1=x2;
        f0=f1;
        f1=poly(xs,x1);
    }
    return x1;
}


