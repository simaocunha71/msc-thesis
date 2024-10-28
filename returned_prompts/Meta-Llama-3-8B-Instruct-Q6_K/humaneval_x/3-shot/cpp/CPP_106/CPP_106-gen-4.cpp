    vector<int> result(n);
    int i;
    for (i=0;i<n;i++)
    {
        if (i%2==0)
            result[i]=factorial(i);
        else
            result[i]=sum(i);
    }
    return result;
}

int factorial(int n)
{
    int i;
    int result=1;
    for (i=2;i<=n;i++)
    {
        result*=i;
    }
    return result;
}

int sum(int n)
{
    int i;
    int result=0;
    for (i=1;i<=n;i++)
    {
        result+=i;
    }
    return result;
}
