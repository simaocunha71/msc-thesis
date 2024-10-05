    double x=0.0;
    double tolerance=0.00001;
    double step=0.00001;
    double f0, f1;
    int i;
    for (i=0;i<xs.size();i++)
    {
        if (i!=0)
        x+=step;
    }
    f0=poly(xs,x);
    while (fabs(f0)>tolerance)
    {
        f1=poly(xs,x);
        x=x-step*f0/f1;
        f0=f1;
    }
    return x;
}
// END OF CODE
// END OF CODE
// END OF CODE
// END OF CODE
// END OF CODE
// END OF CODE
// END OF CODE
// END OF CODE
// END OF CODE
// END OF CODE
// END OF CODE
// END OF CODE
// END OF CODE
// END OF CODE
// END OF CODE
// END OF CODE
// END OF CODE
// END OF CODE
// END OF CODE
// END OF CODE
// END OF CODE
// END OF CODE
// END OF CODE
// END OF CODE
// END OF CODE
// END OF CODE
// END OF CODE
// END OF CODE
// END OF CODE
// END OF CODE
// END OF CODE
// END OF CODE
// END OF CODE
// END OF CODE
// END OF CODE
// END OF CODE
// END OF CODE
// END OF CODE
// END OF CODE
// END OF CODE
// END OF CODE
// END OF CODE
// END OF CODE
// END OF CODE
// END OF CODE
// END OF CODE
// END OF CODE
// END OF CODE
// END OF CODE
// END OF CODE
// END OF CODE
// END OF CODE
// END OF CODE
// END OF CODE
// END OF CODE
// END OF CODE
// END OF CODE
// END OF CODE
// END OF CODE
// END OF CODE
// END OF CODE
// END OF CODE
// END OF CODE
// END OF CODE
// END OF CODE
// END OF CODE
// END OF CODE
// END OF CODE
// END OF CODE
// END OF CODE
// END OF CODE
// END OF CODE
// END OF CODE
// END OF CODE
// END OF CODE
// END OF CODE
// END OF CODE
// END OF CODE
// END OF CODE