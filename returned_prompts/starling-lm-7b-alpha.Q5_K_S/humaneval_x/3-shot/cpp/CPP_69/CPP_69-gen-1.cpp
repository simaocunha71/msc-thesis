    int i,max_num=-1,max_freq=-1;
    for (i=0;i<lst.size();i++)
    {
        int num=lst[i];
        int freq=0;
        for (int j=0;j<lst.size();j++)
        if (num==lst[j]) freq+=1;
        if (freq>=num && num>max_num) max_num=num;
    }
    if (max_num==-1) return -1;
    return max_num;
}



