    sort(l.begin(),l.end());
    vector<int> unique_list;
    int i;
    for (i=0;i<l.size()-1;i++)
    if (l[i]!=l[i+1])
    unique_list.push_back(l[i]);
    unique_list.push_back(l[l.size()-1]);
    return unique_list;
}