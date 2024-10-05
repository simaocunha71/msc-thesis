    float temp;
    if  (a>b && a>c)
    {
        temp=a*a;
        a=c;
        c=temp;
    }
    else if  (b>a && b>c)
    {
        temp=b*b;
        b=c;
        c=temp;
    }
    return (c*c==a*a+b*b);
}


