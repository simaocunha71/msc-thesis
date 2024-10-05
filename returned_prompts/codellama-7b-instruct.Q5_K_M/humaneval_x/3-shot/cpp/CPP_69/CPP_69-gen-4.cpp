    int i, j;
    int max_freq=0;
    int max_val=0;
    for (i=0;i<lst.size();i++)
    {
        int freq=0;
        for (j=0;j<lst.size();j++)
        if (lst[j]==lst[i])
        freq+=1;
        if (freq>max_freq)
        {
            max_freq=freq;
            max_val=lst[i];
        }
    }
    if (max_val>=1)
    return max_val;
    else
    return -1;
}


