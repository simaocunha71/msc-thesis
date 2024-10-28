    int count=0;
    vector<int> arr(n);
    for (int i=0;i<n;i++)
    {
        arr[i]=i*i-i+1;
    }
    for (int i=0;i<n;i++)
    {
        for (int j=i+1;j<n;j++)
        {
            for (int k=j+1;k<n;k++)
            {
                if ((arr[i]+arr[j]+arr[k])%3==0)
                {
                    count+=1;
                }
            }
        }
    }
    return count;
}

