    int i,j,max_freq=0,max_num=-1;
    for (i=0;i<lst.size();i++)
    {
        j=1;
        while (i+j<lst.size()&&lst[i]+j<lst.size())
        {
            if (lst[i]==lst[i+j])
            j++;
        }
        if (j>max_freq)
        {
            max_freq=j;
            max_num=lst[i];
        }
    }
    if (max_num<0)
    return -1;
    else
    return max_num;
}



