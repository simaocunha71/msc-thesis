    int i;
    int current_freq=0;
    int max_freq=0;
    int max_int=0;
    for (i=0;i<lst.size();i++)
    {
        current_freq=0;
        for (int j=0;j<lst.size();j++)
        if (lst[i]==lst[j])
        current_freq++;
        if (current_freq>max_freq)
        {
        max_freq=current_freq;
        max_int=lst[i];
        }
    }
    if (max_freq>=max_int)
    return -1;
    return max_int;
}











