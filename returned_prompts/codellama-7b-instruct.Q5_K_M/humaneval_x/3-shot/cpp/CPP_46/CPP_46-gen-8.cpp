    int i,j,k,l,temp;
    int fib[100];
    int sum;
    sum=0;
    for (i=0;i<4;i++)
        fib[i]=0;
    for (i=4;i<=n;i++)
    {
        j=i-1;
        k=i-2;
        l=i-3;
        fib[i]=fib[j]+fib[k]+fib[l];
        sum+=fib[i];
    }
    return sum;
}



