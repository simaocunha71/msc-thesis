    vector<int> all;
    int i,j;
    for (i=1;i<=n;i++)
    {
        if (i%2==0){
        all.push_back(i);
        for (j=1;j<=i;j++)
        all.push_back(j);
        }
        else
        {
        int sum=0;
        for (j=1;j<=i;j++)
        sum+=j;
        all.push_back(sum);
        }
    }
    return all;
}


