    int max=-1;
    for (int i=0;i<lst.size();i++)
    if (lst[i]>max)
    max=lst[i];
    int sum=0;
    while (max>1)
    {
        if (max%2==1)
        sum+=max;
        max=max/2;
    }
    return sum;
}

