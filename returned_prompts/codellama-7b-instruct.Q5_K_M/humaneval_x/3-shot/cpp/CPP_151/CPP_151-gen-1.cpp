    int i;
    long long sum=0;
    for (i=0;i<lst.size();i++)
    {
        if (abs(lst[i])==int(abs(lst[i])) && lst[i]>0)
        sum+=(lst[i]*lst[i]);
    }
    return sum;
}


