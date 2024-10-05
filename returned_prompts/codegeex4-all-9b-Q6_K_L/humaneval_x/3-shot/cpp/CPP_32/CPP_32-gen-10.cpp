    double x;
    double diff;
    int i;
    int j;
    int k;
    int n=xs.size();
    double sum;
    for (i=0;i<n;i++)
    if (xs[i]!=0)
    break;
    k=i;
    for (i=k+1;i<n;i++)
    if (xs[i]!=0)
    {
        j=i;
        break;
    }
    for (x=0;x<1;x+=0.1)
    {
        sum=0;
        for (i=0;i<n;i++)
        sum+=xs[i]*pow(x,i);
        diff=sum;
        if (diff>0)
        break;
    }
    for (x=0;x<1;x+=0.001)
    {
        sum=0;
        for (i=0;i<n;i++)
        sum+=xs[i]*pow(x,i);
        diff=sum;
        if (diff<0)
        break;
    }
    return x;

}

