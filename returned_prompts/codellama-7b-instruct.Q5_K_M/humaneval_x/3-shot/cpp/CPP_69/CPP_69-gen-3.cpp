    int i,j;
    int max_num=0;
    int max_freq=0;
    int freq;
    for (i=0;i<lst.size();i++)
    {
        freq=0;
        for (j=0;j<lst.size();j++)
        {
            if (lst[j]==lst[i])
            freq+=1;
        }
        if (freq>max_freq)
        {
            max_freq=freq;
            max_num=lst[i];
        }
        if (max_freq>=max_num)
        return max_num;
        else 
        return -1;
    }
}


