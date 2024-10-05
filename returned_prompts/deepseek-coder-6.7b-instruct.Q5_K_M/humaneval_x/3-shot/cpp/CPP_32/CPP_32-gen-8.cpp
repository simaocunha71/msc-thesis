    double low=-1000, high=1000, mid;
    while  (high-low>0.0001)
    {
        mid=(high+low)/2;
        if  (poly(xs, mid)<0)
        low=mid;
        else
        high=mid;
    }
    return low;
}

