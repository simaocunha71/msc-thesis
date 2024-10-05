    int i,j,k;
    int n=lst.size();
    int max=-1;
    for (i=0;i<n;i++)
    {
        if (lst[i]>max)
        {
            max=lst[i];
        }
    }
    int sum=0;
    while (max>0)
    {
        sum+=max%10;
        max=max/10;
    }
    return sum;
}



