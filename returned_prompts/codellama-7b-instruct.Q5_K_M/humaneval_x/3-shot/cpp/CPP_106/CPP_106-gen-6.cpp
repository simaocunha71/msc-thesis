    vector<int> output;
    int sum;
    int i;
    for (i=1;i<=n;i++)
    {
        sum=0;
        if (i%2==0)
        sum=i;
        else
        for (int j=1;j<=i;j++)
        sum+=j;
        output.push_back(sum);
    }
    return output;
}




