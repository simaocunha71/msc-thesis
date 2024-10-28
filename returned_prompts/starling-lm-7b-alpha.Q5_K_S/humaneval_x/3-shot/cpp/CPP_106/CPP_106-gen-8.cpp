    vector<int> res;
    int i;
    for (i=1;i<=n;i++)
    {
        if (i%2==0)
        res.push_back(i);
        else
        {
            int sum=0;
            for (int j=1;j<=i;j++)
            sum+=j;
            res.push_back(sum);
        }
    }
    return res;
}



