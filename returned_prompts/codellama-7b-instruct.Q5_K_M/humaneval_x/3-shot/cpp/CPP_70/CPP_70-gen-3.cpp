    vector<int> new_lst;
    int i;
    for (i=0;i<lst.size();i++)
    if (lst[i]==*min_element(lst.begin(),lst.end()))
    new_lst.push_back(lst[i]);
    lst.erase(remove(lst.begin(),lst.end(),lst[i]),lst.end());

    for (i=0;i<lst.size();i++)
    if (lst[i]==*max_element(lst.begin(),lst.end()))
    new_lst.push_back(lst[i]);
    lst.erase(remove(lst.begin(),lst.end(),lst[i]),lst.end());

    for (i=0;i<lst.size();i++)
    if (lst[i]==*min_element(lst.begin(),lst.end()))
    new_lst.push_back(lst[i]);
    lst.erase(remove(lst.begin(),lst.end(),lst[i]),lst.end());

    return new_lst;
}


