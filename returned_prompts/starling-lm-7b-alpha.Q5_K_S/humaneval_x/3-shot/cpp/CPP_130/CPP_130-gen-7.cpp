    vector<int> result;
    int a,b,c;
    if (n==0)
    {
        result.push_back(0);
        return result;
    }
    if (n==1)
    {
        result.push_back(1);
        result.push_back(3);
        return result;
    }
    if (n%2==0)
    {
        result.push_back(3);
        result.push_back(1);
        for (int i=3;i<=n;i++)
        {
            a=result[i-1];
            b=result[i-2];
            c=result[i-3];
            result.push_back(c+a+b);
        }
    }
    if (n%2!=0)
    {
        result.push_back(1);
        result.push_back(3);
        result.push_back(2);
        for (int i=4;i<=n;i++)
        {
            a=result[i-1];
            b=result[i-2];
            c=result[i-3];
            result.push_back(c+a+b);
        }
    }
    return result;
}


