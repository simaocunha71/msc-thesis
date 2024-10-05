    vector<int> res;
    for (int i=0;i<lst.size();i++)
    if (lst[i]==*min_element(lst.begin(),lst.end()))
    res.push_back(lst[i]);
    for (int i=0;i<lst.size();i++)
    if (lst[i]==*max_element(lst.begin(),lst.end()))
    res.push_back(lst[i]);
    for (int i=0;i<lst.size();i++)
    if (lst[i]!=*max_element(lst.begin(),lst.end()) && lst[i]!=*min_element(lst.begin(),lst.end()))
    res.push_back(lst[i]);
    return res;
}


