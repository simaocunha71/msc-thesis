    vector<int> res;
    for (int i=1;i<=n;i++)
    {
        if (i%2==0)
        res.push_back(i);
        else
        res.push_back(i*i);
    }
    return res;
}


