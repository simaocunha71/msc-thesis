    sort(l.begin(),l.end());
    vector<int> unique_list;
    unique_list.push_back(l[0]);
    for (int i=1;i<l.size();i++)
    if (l[i]!=l[i-1])
    unique_list.push_back(l[i]);
    return unique_list;
}

