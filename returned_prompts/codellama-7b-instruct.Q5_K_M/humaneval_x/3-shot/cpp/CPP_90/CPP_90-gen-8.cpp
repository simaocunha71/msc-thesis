    if (lst.size()<2)
    return -1;
    auto it=min_element(lst.begin(),lst.end());
    int min=*it;
    int idx=it-lst.begin();
    if (idx+1<lst.size())
    return lst[idx+1];
    else
    return -1;
}



