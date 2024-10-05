    int i,max_freq=0,max_val=-1;
    for (i=0;i<lst.size();i++)
    {
        if (lst[i]>max_val && lst[i]<=i+1)
        {
            if (max_freq<(lst[i]/lst[i]))
            {
                max_val=lst[i];
                max_freq=lst[i]/lst[i];
            }
        }
    }
    return max_val;
}

