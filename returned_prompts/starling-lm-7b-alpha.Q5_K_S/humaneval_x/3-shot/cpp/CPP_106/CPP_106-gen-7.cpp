    vector<int> result;
    int i,j;
    int fact=1;
    for (i=1;i<=n;i++)
    {
        result.push_back(i%2==0?fact:0);
        if (i%2!=0)
        for (j=1;j<=i;j++)
        fact+=j;
    }
    return result;
}


