    int fib1,fib2;
    int i;
    int count=1;
    int flag=0;
    fib1=0;
    fib2=1;
    for (i=0;i<=n;i++)
    {
        if (fib1==1)
            break;
        int temp=fib1;
        fib1=fib2;
        fib2=temp+fib2;

        for (int j=2;j<fib1;j++)
        {
            if (fib1%j==0)
            {
                flag=1;
                break;
            }
            flag=0;
        }
        if (flag==0)
            count+=1;
    }
    return fib1;
}

