    int i,count;
    int max=-1;
    for (i=0;i<lst.size();i++)
    {
        count=0;
        for (int j=0;j<lst.size();j++)
        if (lst[i]==lst[j])
        count+=1;
        if (count>=lst[i] && lst[i]>max)
        max=lst[i];
    }
    return max;
}




