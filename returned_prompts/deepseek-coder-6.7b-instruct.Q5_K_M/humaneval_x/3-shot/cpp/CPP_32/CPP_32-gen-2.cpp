    double start=-10000;
    double end=10000;
    double mid;
    while ((end-start)>0.00001)
    {
        mid=(start+end)/2;
        if  (poly(xs,mid)>0)
        {
            end=mid;
        }
        else
        {
            start=mid;
        }
    }
    return start;
}

