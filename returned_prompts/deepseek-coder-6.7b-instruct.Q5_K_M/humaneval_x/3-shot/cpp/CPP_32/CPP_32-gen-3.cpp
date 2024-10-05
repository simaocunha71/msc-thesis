    double start=-100000, end=100000, mid;
    while  (end-start>0.000001){
        mid=(start+end)/2;
        if  (poly(xs, mid)<0)
            start=mid;
        else
            end=mid;
    }
    return start;
}


