    int i,j;
    int max=-1;
    int count=0;

    for (i=0;i<lst.size();i++)
    {
        count=0;
        for (j=0;j<lst.size();j++)
        {
            if (lst[i]==lst[j])
            count+=1;
        }
        if (count>=lst[i])
        {
            max=lst[i];
        }
    }
    return max;
}

