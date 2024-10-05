    int i,j, max=0;
    for (i=0;i<lst.size();i++)
    {
        for (j=2;j<lst[i];j++)
        {
            if (lst[i]%j==0)
            break;
        }
        if (j==lst[i] && lst[i]>max)
        max=lst[i];
    }
    int sum=0;
    while (max>0)
    {
        sum+=max%10;
        max=max/10;
    }
    return sum;
}

