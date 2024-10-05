    int i=2;
    int fib1=0;
    int fib2=1;
    int fib3;
    int prime_count=0;
    while(prime_count<n)
    {
        fib3=fib1+fib2;
        fib1=fib2;
        fib2=fib3;
        for(int j=2;j<fib3;j++)
        {
            if(fib3%j==0)
            {
                break;
            }
            if(j==fib3-1)
            {
                prime_count++;
                if(prime_count==n)
                {
                    return fib3;
                }
            }
        }
    }
}


