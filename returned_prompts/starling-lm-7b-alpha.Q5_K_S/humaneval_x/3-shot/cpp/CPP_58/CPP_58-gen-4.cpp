    vector<int> common_list;
    vector<int>::iterator it;
    for (it=l1.begin();it!=l1.end();it++)
    if (binary_search(l2.begin(),l2.end(),*it))
    {
        common_list.push_back(*it);
    }

    sort(common_list.begin(),common_list.end());
    common_list.erase(unique(common_list.begin(),common_list.end()),common_list.end());

    return common_list;
}

