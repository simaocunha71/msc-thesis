    vector<int> result;
    int i;
    result.push_back(3);
    if (n==0)
        return result;
    if (n==1)
    {
        result.push_back(1);
        return result;
    }
    if (n==2)
    {
        result.push_back(2);
        return result;
    }
    result.push_back(1);
    result.push_back(3);
    for (i=3;i<=n;i++)
    {
        if (i%2==0)
        {
            result.push_back(3);
        }
        if (i%2==1)
        {
            result.push_back(result[i-1]+result[i-2]+result[i+1]);
        }
    }
    return result;
}


