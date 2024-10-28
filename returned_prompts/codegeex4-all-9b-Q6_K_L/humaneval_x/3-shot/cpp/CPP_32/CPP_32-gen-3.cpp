    double x1=0;
    double x2=1;
    double y1=poly(xs,x1);
    double y2=poly(xs,x2);
    while (abs(y1)>0.00001)
    {
        x1=x2;
        x2+=0.00001;
        y1=poly(xs,x1);
        y2=poly(xs,x2);
    }
    return x2;
}

