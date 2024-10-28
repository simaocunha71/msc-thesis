    int a=0,b=0,c=1,i;
    if (n<3){
        return n;
    }
    for (i=3;i<=n;i++)
    {
        c=a+b;
        a=b;
        b=c;
    }
    return c;
}

