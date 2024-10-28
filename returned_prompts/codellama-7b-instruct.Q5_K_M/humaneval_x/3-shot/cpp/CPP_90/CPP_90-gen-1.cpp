    if (lst.size()==1)
    return -1;
    else
    sort(lst.begin(),lst.end());
    for (int i=0;i<lst.size();i++)
    if (i<lst.size()-1)
    if (lst[i+1]>lst[i])
    return lst[i];
    return -1;
}



