    vector<int> result;
    int i;
    for (i=1;i<=n;i++)
    {
        if (i%2==0)
        result.push_back(i);
        else
        result.push_back(i*(i+1)/2);
    }
    return result;
}


