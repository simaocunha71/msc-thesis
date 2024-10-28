    int i;
    long long sum=0;
    for (i=0;i<lst.size();i++)
    {
        if (lst[i]>=0 && lst[i]-int(lst[i])==0)
        sum+=pow(lst[i],2);
    }
    return sum;
}




