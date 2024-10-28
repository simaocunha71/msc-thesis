    vector<int> result;
    int i;
    for (i=0;i<n;i++)
    {
        if (i%2==0)
        result.push_back(i);
        else
        {
            int sum=0;
            int j;
            for (j=1;j<=i;j++)
            sum+=j;
            result.push_back(sum);
        }
    }
    return result;
}


