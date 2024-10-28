    long long sum=0;
    for (int i=0;i<lst.size();i++)
    {
        if (lst[i]>0 && modf(lst[i], &lst[i])==0)
        sum+=pow(lst[i],2);
    }
    return sum;
}