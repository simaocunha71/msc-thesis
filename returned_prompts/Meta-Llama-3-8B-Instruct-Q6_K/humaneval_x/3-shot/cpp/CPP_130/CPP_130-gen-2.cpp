    vector<int> result;
    result.push_back(3);
    if (n>0)
    {
        result.push_back(1);
        if (n>1)
        {
            result.push_back(1);
            for (int i=3;i<=n;i++)
            {
                result.push_back(result[i-1]+result[i-2]+result[i-3]);
            }
        }
    }
    return result;
}