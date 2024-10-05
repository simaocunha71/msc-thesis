    vector<int> result;
    result.push_back(1);
    result.push_back(3);
    result.push_back(2);
    result.push_back(8);
    if (n==3)
    return result;
    if (n%2==0)
    {
        for (int i=4;i<=n;i++)
        {
            result.push_back(1+(i/2));
        }
    }
    if (n%2!=0)
    {
        for (int i=4;i<=n;i++)
        {
            result.push_back(result[i-1]+result[i-2]+result[i-3]);
        }
    }
    return result;
}











