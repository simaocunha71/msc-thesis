    int max=-1;
    int i;
    for (i=0;i<lst.size();i++)
    {
        int count=0;
        int j;
        for (j=0;j<lst.size();j++)
        {
            if (lst[i]==lst[j])
            {
                count+=1;
            }
        }
        if (count>=lst[i])
        {
            max=lst[i];
        }
    }
    return max;
}

