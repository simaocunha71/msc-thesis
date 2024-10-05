    int i;
    long long int sum=0;
    for (i=0;i<lst.size();i++)
    {
        if (lst[i]<0 || lst[i]-int(lst[i])>0)
        continue;
        sum+=(int(lst[i])*(int(lst[i])));
    }
    return sum;
}

