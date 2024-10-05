    int i;
    double start,end;
    double mid;
    double sum;
    double sum1,sum2;
    double epsilon=1e-5;
    for (i=0;i<xs.size()-1;i++)
    {
        if (xs[i]!=0)
        {
            start=i;
            end=i+1;
            break;
        }
    }
    while (end-start>1){
        mid=(start+end)/2;
        sum1=poly(xs,start);
        sum2=poly(xs,end);
        if (sum1*sum2<=0)
        {
            start=mid;
        }
        else{
            end=mid;
        }
    }
    return (start+end)/2;
}

