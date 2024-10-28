    int i;
    int max=0;
    int min=0;
    int max_pos=0;
    int min_pos=0;
    for (i=0;i<lst.size();i++)
    {
        if (lst[i]>=0)
        {
            if (lst[i]<max_pos)
            min_pos=lst[i];
        }
        else if (lst[i]<0)
        {
            if (lst[i]>max)
            max=lst[i];
        }
    }
    return {max,min_pos};
}

