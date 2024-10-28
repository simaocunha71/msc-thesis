    vector<int> common;
    int i;
    for (i=0;i<l1.size();i++)
    if (find(l2.begin(),l2.end(),l1[i])!=l2.end())
    common.push_back(l1[i]);
    sort(common.begin(),common.end());
    common.erase(unique(common.begin(),common.end()),common.end());
    return common;
}



