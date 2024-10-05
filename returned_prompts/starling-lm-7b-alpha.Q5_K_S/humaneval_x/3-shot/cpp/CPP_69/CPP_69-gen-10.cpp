    int i;
    int freq, max_freq, max_val;
    max_freq=0;
    for (i=0;i<lst.size();i++)
    {
        freq=0;
        for (int j=0;j<lst.size();j++)
        if (lst[i]==lst[j])
        freq+=1;

        if (freq>max_freq && lst[i]>max_freq)
        {
            max_freq=freq;
            max_val=lst[i];
        }
    }

    if (max_val>max_freq)
    return -1;
    else
    return max_val;
}




