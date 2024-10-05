    int i,j,max_val=-1;
    int freq;
    for (i=0;i<lst.size();i++)
    {
        freq=0;
        for (j=0;j<lst.size();j++)
        if (lst[i]==lst[j])
        freq+=1;
        if (freq>lst[i]&&max_val<lst[i])
        max_val=lst[i];
    }
    return max_val;
}



