    int i,j;
    int max=0;
    int count=0;
    for (i=0;i<lst.size();i++)
    {
        count=0;
        for (j=0;j<lst.size();j++)
        if (lst[j]==lst[i])
        count+=1;
        if (count>=lst[i]&&lst[i]>max)
        max=lst[i];
    }
    if (max>0)
    return max;
    else
    return -1;
}

