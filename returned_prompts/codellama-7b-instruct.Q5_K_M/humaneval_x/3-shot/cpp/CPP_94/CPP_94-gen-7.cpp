    int max=0,sum=0;
    for (int i=0;i<lst.size();i++)
    {
        if (lst[i]>max)
        max=lst[i];
    }
    int temp=max;
    while (temp>0)
    {
        sum+=temp%10;
        temp/=10;
    }
    return sum;
}






