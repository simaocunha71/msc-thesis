    int prod=1;
    long long sum=0;
    int i;
    if (arr.empty())
        return -32768;
    for (i=0;i<arr.size();i++)
    {
        if (arr[i]==0)
        {
            return 0;
        }
        prod=prod*abs(arr[i]);
        if (arr[i]>0)
            sum+=abs(arr[i]);
        else
            sum-=abs(arr[i]);
    }
    return prod*(sum);
}
```




