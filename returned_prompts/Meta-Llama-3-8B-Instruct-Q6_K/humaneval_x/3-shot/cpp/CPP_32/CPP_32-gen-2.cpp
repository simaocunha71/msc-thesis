    double x=-1;
    double dx=0.1;
    double f0,p0;
    int i;
    f0=poly(xs,x);
    while (fabs(f0)>1e-6)
    {
        p0=f0;
        x+=dx;
        f0=poly(xs,x);
    }
    return x;
}