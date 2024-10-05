    long long sum=0;
    int i;
    for (i=0;i<lst.size();i++)
    {
        if (lst[i]<0)
        continue;
        if (floor(lst[i])!=lst[i])
        continue;
        if (lst[i]%2==0)
        continue;
        sum=sum+lst[i]*lst[i]*2;
    }
    return sum;
}