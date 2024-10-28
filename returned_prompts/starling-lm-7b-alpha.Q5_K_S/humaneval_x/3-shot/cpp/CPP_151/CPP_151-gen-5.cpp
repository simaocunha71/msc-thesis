    long long sum=0;
    int i;
    int j;
    for (i=0;i<lst.size();i++)
    {
        if (lst[i]>0 && (int)lst[i]==lst[i])
        sum+=(long long)lst[i]*lst[i];
    }
    return sum;
}



