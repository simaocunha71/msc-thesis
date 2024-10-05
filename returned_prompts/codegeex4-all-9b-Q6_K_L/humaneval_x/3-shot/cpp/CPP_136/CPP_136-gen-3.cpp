    int i;
    int max=0;
    int min=0;
    for (i=0;i<lst.size();i++)
    {
        if (lst[i]>0)
        {
            if (lst[i]<min || min==0)
            min=lst[i];
        }
        if (lst[i]<0)
        {
            if (lst[i]>max || max==0)
            max=lst[i];
        }
    }
    return {max,min};
}

