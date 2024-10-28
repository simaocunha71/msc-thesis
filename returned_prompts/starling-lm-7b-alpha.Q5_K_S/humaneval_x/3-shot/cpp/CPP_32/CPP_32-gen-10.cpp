    double a;
    double x;
    double y;
    double f_x;
    double f_y;
    double mid;
    int i;
    for (i=0;i<xs.size();i++)
    {
        a=xs[i];
    }
    x=-a/(2*xs[0]);
    f_x=poly(xs,x);
    y=0;
    while (abs(f_x)>0.0001)
    {
        mid=(x+y)/2;
        f_y=poly(xs,mid);
        if (f_y==0)
        {
            return mid;
        }
        if (f_y<0)
        {
            x=mid;
        }
        else
        {
            y=mid;
        }
    }
    return mid;
}


