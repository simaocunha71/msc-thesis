    int i;
    int n=lst.size();
    int max_freq=-1;
    int max_val=-1;
    for (i=0;i<n;i++)
    {
        int val=lst[i];
        int freq=0;
        for (int j=0;j<n;j++)
        {
            if (lst[j]==val)
            freq+=1;
        }
        if (freq>val)
        {
        if (freq>max_freq){
            max_freq=freq;
            max_val=val;
        }
        }
    }
    if (max_freq==-1)
    return -1;
    else
    return max_val;
}



