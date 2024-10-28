    int i;
    if (lst.size()<2)
    return -1;
    sort(lst.begin(),lst.end());
    for (i=0;i<lst.size()-1;i++)
    if (lst[i+1]!=lst[i])
    return lst[i+1];
    return -1;
}



