    double x1=0.0;
    double x2=1.0;
    double fx1=poly(xs,x1);
    double fx2=poly(xs,x2);

    while (abs(fx1)>0.01)
    {
        x1=x2;
        fx1=fx2;
        x2=x1+0.1;
        fx2=poly(xs,x2);
    }

    return x2;

}

