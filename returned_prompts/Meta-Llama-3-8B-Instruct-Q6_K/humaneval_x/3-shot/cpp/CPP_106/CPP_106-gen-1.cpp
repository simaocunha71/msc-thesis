    vector<int> result;
    int i;
    for (i=1;i<=n;i++)
    {
        if (i%2==0)
            result.push_back(factorial(i));
        else
            result.push_back(sum(1,i));
    }
    return result;
}

int factorial(int n)
{
    int i;
    int f=1;
    for (i=1;i<=n;i++)
        f *= i;
    return f;
}

int sum(int start, int end)
{
    int i;
    int s=0;
    for (i=start;i<=end;i++)
        s += i;
    return s;
}