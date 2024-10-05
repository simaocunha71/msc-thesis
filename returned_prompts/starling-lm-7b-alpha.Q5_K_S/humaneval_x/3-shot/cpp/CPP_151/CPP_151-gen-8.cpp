    long long int sum=0;
    int i;
    for (i=0;i<lst.size();i++)
    if (int(lst[i])%2==1)
    sum+=pow(lst[i],2);
    return sum;
}


