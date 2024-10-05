    int n=xs.size();
    if  (n==2)
    {
        return -xs[0]/xs[1];
    }
    else
    {
        double a=xs[n-2];
        double b=xs[n-1];
        double c=xs[0];
        double q=(a+b)/2;
        double r=(b-a)/2;
        double f=c-poly(xs,q);
        while  (fabs(f)>1e-6){
            if (f>0)
                r*=2;
            else
                q*=2;
            f=c-poly(xs,q);
        }
        return q;
    }
}


