    vector<int> result(n);
    int i;
    int j;
    int sum;
    for (i=1;i<n;i++)
    {
        if (i%2==0)
        result[i]=i;
        else
        {
            sum=0;
            for (j=1;j<=i;j++)
            sum+=j;
            result[i]=sum;
        }
    }
    return result;
}



