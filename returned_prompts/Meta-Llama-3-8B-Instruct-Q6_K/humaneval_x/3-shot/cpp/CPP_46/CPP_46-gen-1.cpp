    int a=0,b=0,c=2,d=0;
    for (int i=3;i<=n;i++)
    {
        int temp=a+b+c;
        a=b;c=d;b=temp;d=temp;
    }
    return d;
}