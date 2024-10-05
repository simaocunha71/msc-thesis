    int i;
    int j;
    int max=0;
    for (i=0;i<lst.size();i++)
    if (lst[i]>max)
    max=lst[i];
    for (j=0;j<lst.size();j++)
    if (lst[j]==max)
    break;
    int num=lst[j];
    int sum=0;
    while (num>0)
    {
    sum+=num%10;
    num=num/10;
    }
    return sum;
}

