    vector<int> fib;
    int i,j,k;
    int fibo=0;
    int prime=false;
    int count=0;

    fib.push_back(0);
    fib.push_back(1);
    while (count<n)
    {
        fibo=fib[i]+fib[j];
        fib.push_back(fibo);
        i+=1;
        j+=1;
        count+=1;
    }
    for (i=0;i<fib.size();i++)
    {
        if (fib[i]>1)
        {
        prime=true;
        for (j=2;j<sqrt(fib[i])+1;j++)
        {
            if (fib[i]%j==0)
            {
            prime=false;
            break;
            }
        }
        if (prime==true)
        {
        return fib[i];
        }
        }
    }
}



