    int i;
    double x;
    double b=xs[xs.size()-1];
    double a=xs[xs.size()-2];
    if (a==0) return -b/b;
    if (b==0) return -a/a;
    if (a*b<0) return -a/b;
    if (abs(a)>=abs(b))
    {
        x=-a/b;
        if (poly(xs,x)==0) return x;
        for (i=xs.size()-3;i>=0;i--)
        {
            if (xs[i]==0) continue;
            x-=poly(xs,x)/xs[i];
            if (poly(xs,x)==0) return x;
        }
    }
    else
    {
        x=-b/a;
        if (poly(xs,x)==0) return x;
        for (i=xs.size()-3;i>=0;i--)
        {
            if (xs[i]==0) continue;
            x-=poly(xs,x)/xs[i];
            if (poly(xs,x)==0) return x;
        }
    }
    return x;
}


