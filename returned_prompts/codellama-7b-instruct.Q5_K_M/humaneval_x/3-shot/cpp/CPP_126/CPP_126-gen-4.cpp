    if (lst.size()<2)
    return true;
    vector<int>::iterator it=unique(lst.begin(),lst.end());
    if (it!=lst.end())
    return false;
    vector<int>::iterator it2=min_element(lst.begin(),lst.end());
    vector<int>::iterator it3=max_element(lst.begin(),lst.end());
    if (*it3<*it2)
    return false;
    return true;
}



