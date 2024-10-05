    vector<string> sorted_list;
    vector<string>::iterator it;
    sort(lst.begin(),lst.end());
    for (it=lst.begin();it!=lst.end();it++)
    if ((*it).size()%2==0)
    sorted_list.push_back(*it);
    sort(sorted_list.begin(),sorted_list.end());
    return sorted_list;
}

