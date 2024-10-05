    if(n<0)
    {
        printf("n should be a positive integer");
        return -1;
    }
    if(n<=3)
    {
        if(n==0 || n==1)
        {
            return 0;
        }
        else if(n==2)
        {
            return 2;
        }
        else
        {
            return 0;
        }
    }
    else
    {
        int a=0,b=0,c=2,d=0;
        for(int i=3;i<=n;i++)
        {
            int temp=a+b+c+d;
            a=b;c=d;b=temp%10;
            d=temp/10;
        }
        return d*10+b;
    }
}
