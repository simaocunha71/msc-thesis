    vector<int> result;
    for (int i=1;i<=n;i++)
    {
        if (i%2==0)
            result.push_back(factorial(i));
        else
            result.push_back(sum(i));
    }
    return result;
}

int factorial(int n)
{
    int res = 1;
    for (int i = 1; i <= n; ++i)
        res *= i;
    return res;
}

int sum(int n)
{
    int res = 0;
    for (int i = 1; i <= n; ++i)
        res += i;
    return res;
}