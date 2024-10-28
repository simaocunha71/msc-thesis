    vector<int> result;
    int d,i;
    for (d=2;d*d<=n;d++)
    {
        while (n%d==0)
        {
            result.push_back(d);
            n/=d;
        }
    }
    if (n>1)
    {
        result.push_back(n);
    }
    return result;
}


