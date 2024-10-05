    double a=1.0, b=2.0, c, d=0.00001;
    c=a+(b-a)/2;
    while  ((poly(xs,a)*poly(xs,c))>d)
    {
        if ((poly(xs,a)*poly(xs,c))<-d)
            a=c;
        else
            b=c;
        c=a+(b-a)/2;
    }
    return c;
}


