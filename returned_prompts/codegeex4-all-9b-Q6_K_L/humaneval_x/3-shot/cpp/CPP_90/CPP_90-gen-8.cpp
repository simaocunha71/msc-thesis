    sort(lst.begin(),lst.end());
    int i;
    for (i=1;i<lst.size();i++)
    if (lst[i]!=lst[i-1])
    return lst[i];
    return -1;
}

