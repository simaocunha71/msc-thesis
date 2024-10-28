    if (lst.size()<2) return -1;
    int min_idx=0;
    for (int i=0;i<lst.size();i++)
    if (lst[i]<lst[min_idx])
    min_idx=i;
    for (int i=0;i<lst.size();i++)
    if (lst[i]==lst[min_idx])
    return lst[i+1];
    return -1;
}



