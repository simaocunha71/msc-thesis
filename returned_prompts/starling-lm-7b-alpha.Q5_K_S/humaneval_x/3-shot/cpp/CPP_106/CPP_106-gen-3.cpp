    vector<int> result;
    int i;
    for (i=0;i<n;i++)
    {
        if (i%2==0)
        {
        result.push_back(i);
        for (int j=i;j>1;j--)
        result.push_back(result.back()*j);
        }
        else
        {
        result.push_back(0);
        for (int j=1;j<=i;j++)
        result.push_back(result.back()+j);
        }
    }
    return result;
}


