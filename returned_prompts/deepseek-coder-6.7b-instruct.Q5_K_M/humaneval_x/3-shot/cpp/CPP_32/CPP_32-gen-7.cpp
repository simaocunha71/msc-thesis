    double start=-10000;
    double end=10000;
    double mid=(start+end)/2;
    while(poly(xs, mid)!=0)
    {
        if(poly(xs, mid)>0)
        {
            start=mid;
        }
        else
        {
            end=mid;
        }
        mid=(start+end)/2;
    }
    return mid;
}

