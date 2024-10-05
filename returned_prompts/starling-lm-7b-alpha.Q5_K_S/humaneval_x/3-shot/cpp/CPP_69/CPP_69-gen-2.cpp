    int i,j,max_num=-1,max_freq=-1,num,freq;
    for (i=0;i<lst.size();i++)
    {
        num=lst[i];
        freq=0;
        for (j=0;j<lst.size();j++)
        if (lst[j]==num)
        freq+=1;
        if (num>max_num && freq>=num)
        max_num=num;
    }
    if (max_num==-1)
    return -1;
    return max_num;
}



