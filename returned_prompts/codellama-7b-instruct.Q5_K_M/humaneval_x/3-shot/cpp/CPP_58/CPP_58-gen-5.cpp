    vector<int> l1_common;
    vector<int> l2_common;
    vector<int> common_l1_l2;

    for (int i=0;i<l1.size();i++)
    for (int j=0;j<l2.size();j++)
    {
        if (l1[i]==l2[j])
        {
            l1_common.push_back(l1[i]);
            l2_common.push_back(l2[j]);
        }
    }

    for (int i=0;i<l1_common.size();i++)
    for (int j=0;j<l2_common.size();j++)
    {
        if (l1_common[i]==l2_common[j])
        common_l1_l2.push_back(l1_common[i]);
    }

    sort(common_l1_l2.begin(),common_l1_l2.end());
    common_l1_l2.erase(unique(common_l1_l2.begin(),common_l1_l2.end()),common_l1_l2.end());
    return common_l1_l2;
}


