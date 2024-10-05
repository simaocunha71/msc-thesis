    double x=0;
    int i;
    double sum=0;
    for (i=0;i<xs.size();i++)
    {
        sum+=xs[i]*pow(x,i);
    }
    while (abs(sum)>0.00001)
    {
        x=x-1.0*sum/xs[xs.size()-1];
        sum=poly(xs,x);
    }
    return x;
}  // Not finished


