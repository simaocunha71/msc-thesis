    int i,j;
    int min=INT_MAX;
    int second_min=INT_MAX;
    
    for (i=0;i<lst.size();i++)
    {
        if (min>lst[i])
        {
        second_min=min;
        min=lst[i];
        }
    }
    for (i=0;i<lst.size();i++)
    {
        if (lst[i]!=min)
        {
        if (second_min>lst[i])
        second_min=lst[i];
        }
    }
    if (second_min==INT_MAX)
    return -1;
    return second_min;
}

