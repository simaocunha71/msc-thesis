    if (lst.size()==0)
    return true;
    if (lst.size()==1)
    return true;
    if (lst.size()==2)
    return (lst[0]<lst[1]);
    sort(lst.begin(),lst.end());
    int i;
    for (i=0;i<lst.size()-1;i++)
    if (lst[i]==lst[i+1])
    return false;
    return (lst[i]<lst[i+1]);
}


