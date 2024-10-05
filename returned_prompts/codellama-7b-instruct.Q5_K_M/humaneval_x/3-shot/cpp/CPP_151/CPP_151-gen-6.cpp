    int i;
    long long ans=0;
    for (i=0;i<lst.size();i++)
    if (lst[i]>0)
    ans+=pow(lst[i], 2);
    return ans;
}



