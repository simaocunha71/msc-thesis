    if (lst.size()<2)
    return -1;
    sort(lst.begin(),lst.end());
    if (lst.size()==2)
    return lst[1];
    return lst[2];
}



