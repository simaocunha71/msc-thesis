    long long sum=0;
    int i;
    for (i=0;i<lst.size();i++)
    if (lst[i]%2==1 && lst[i]>0)
    sum+=pow(lst[i],2);

    return sum;
}



