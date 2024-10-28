    int t;
    while(a!=0 && b!=0)
    {
        if (a>b)
        {
        t=a;
        a=b;
        b=t;
        }
        t=b%a;
        b=a;
        a=t;
    }
    return a+b;
}



