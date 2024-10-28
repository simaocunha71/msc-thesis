    vector<int> prime;
    int i=0;
    int j=0;
    int flag=0;
    for (i=2;i<n;i++)
    {
        flag=0;
        for (j=2;j<i;j++)
        if (i%j==0)
        {
            flag=1;
            break;
        }
        if (flag==0)
        prime.push_back(i);
    }
    return prime;
}

